import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import re


def clean_text(text: str) -> str:
    if not text:
        return text
    text = re.sub(r'[\uE000-\uF8FF]+', '', text)
    text = text.replace('\uE14D', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

async def scrape_google_maps_async(query="Restaurants chinois Antananarivo", max_result=100):
    results = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        ))
        page = await context.new_page()
        await page.goto("https://www.google.com/maps", timeout=60000, wait_until="domcontentloaded")

        # Accepter les cookies
        for label in ("Tout accepter", "Accept all", "Accepter tout"):
            try:
                await page.click(f"button:has-text('{label}')", timeout=5000)
                break
            except PlaywrightTimeoutError:
                continue

        # Recherche et attente des résultats
        await page.fill("input#searchboxinput", query)
        await page.keyboard.press("Enter")
        await page.wait_for_selector("div[role='feed'] .hfpxzc", timeout=20000)

        scroll_container = page.locator("div[role='feed']")
        for _ in range(3):  # Ajuste selon le nombre de résultats souhaités
            await scroll_container.evaluate("(el) => el.scrollBy(0, 1000)")
            await asyncio.sleep(1)

        link_locators = await page.locator("div[role='feed'] .hfpxzc").all()

        for idx, link in enumerate(link_locators[:max_result]):
            data = { key: None for key in (
                "name","address","phone","hours","weekly_schedule",
                "rating","reviews","service_options","highlights",
                "popular_for","offerings","dining_options","amenities",
                "atmosphere","crowd","children", "latitude", "longitude"
            )}
            data["weekly_schedule"] = {}
            for key in ("service_options","highlights","popular_for","offerings",
                        "dining_options","amenities","atmosphere","crowd","children"):
                data[key] = []

            try:
                href = await link.get_attribute("href")
                if not href:
                    raise ValueError("href manquant")

                # Extraire latitude et longitude à partir du lien
                match = re.search(r'!3d([-\d.]+)!4d([-\d.]+)', href)
                if not match:
                    match = re.search(r'/@([-\d.]+),([-\d.]+)', href)
                if match:
                    data["latitude"] = float(match.group(1))
                    data["longitude"] = float(match.group(2))

                detail = await context.new_page()
                await detail.goto(href, timeout=60000, wait_until="domcontentloaded")

                async def safe_text(locator, method="inner_text", **kwargs):
                    try:
                        txt = (await getattr(locator, method)(**kwargs)) or ""
                        return clean_text(txt)
                    except:
                        return None

                data["name"]    = await safe_text(detail.locator(".DUwDvf"))
                data["address"] = await safe_text(detail.locator('button[data-item-id="address"] .Io6YTe'))
                data["phone"]   = await safe_text(detail.locator('button[data-item-id^="phone"] .Io6YTe'))
                data["hours"]   = await safe_text(detail.locator('.OqCZI .fontBodyMedium'), method="text_content")

                try:
                    table = detail.locator('table.eK4R0e.fontBodyMedium')
                    await table.wait_for(timeout=5000)
                    rows = await table.locator("tbody tr").all()
                    for row in rows:
                        day = clean_text(await row.locator('td:nth-child(1) div').text_content())
                        hr  = clean_text(await row.locator('td:nth-child(2) [role="text"]').text_content())
                        data["weekly_schedule"][day] = hr
                except PlaywrightTimeoutError:
                    pass

                await detail.wait_for_selector(".jANrlb", timeout=5000)
                data["rating"]  = await safe_text(detail.locator(".jANrlb .fontDisplayLarge"))
                data["reviews"] = await safe_text(detail.locator(".jANrlb button span"))

                try:
                    tab = detail.get_by_role("tab", name="About")
                    await tab.wait_for(timeout=5000)
                    await tab.click()
                    await detail.wait_for_selector('h2:has-text("Service options")', timeout=5000)
                except PlaywrightTimeoutError:
                    pass

                for key, label in [
                    ("service_options", "Service options"),
                    ("highlights",     "Highlights"),
                    ("popular_for",    "Popular for"),
                    ("offerings",      "Offerings"),
                    ("dining_options", "Dining options"),
                    ("amenities",      "Amenities"),
                    ("atmosphere",     "Atmosphere"),
                    ("crowd",          "Crowd"),
                    ("children",       "Children"),
                ]:
                    try:
                        items = await detail.locator(f'h2:has-text("{label}") + ul > li').all_text_contents()
                        data[key] = [clean_text(it) for it in items if clean_text(it)]
                    except:
                        pass

                results.append(data)
                await detail.close()

            except Exception as e:
                print(f"[Erreur] lien #{idx} : {e}")
            finally:
                await asyncio.sleep(1)

        await browser.close()
    return results


