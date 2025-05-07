import asyncio
from src.scraping.google_map_scraper import scrape_google_maps_async
from src.data_manip.to_json import extract_json

async def main():
    print("[INFO] Lancement du scraping Google Maps...(Ceci peut prendre quelques minutes)")
    all_data = await scrape_google_maps_async()
    print("[INFO] Scraping terminé.")
    
    print("[INFO] Extraction des données en JSON...")
    # extract_json(all_data)
    print("[INFO] Extraction terminée. Les données ont été sauvegardées.")

if __name__ == "__main__":
    asyncio.run(main())
