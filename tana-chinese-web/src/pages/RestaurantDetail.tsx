
import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import restaurantsData from "@/data/restaurants.json";
import RestaurantMap from "@/components/RestaurantMap";
import Restaurant3DView from "@/components/Restaurant3DView";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { ArrowLeft, MapPin, Map, Star } from "lucide-react";

const RestaurantDetail = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [restaurant, setRestaurant] = useState<any | null>(null);

  useEffect(() => {
    const restaurantId = parseInt(id || "0");
    const foundRestaurant = restaurantsData.find(
      (r) => r.id === restaurantId
    );
    
    if (foundRestaurant) {
      setRestaurant(foundRestaurant);
    }
  }, [id]);

  if (!restaurant) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold mb-4">Restaurant non trouvé</h2>
          <button 
            onClick={() => navigate("/")}
            className="bg-primary text-primary-foreground px-4 py-2 rounded-md"
          >
            Retour à l'accueil
          </button>
        </div>
      </div>
    );
  }

  // Format hours information
  const formatHours = (hoursString: string) => {
    const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    let formattedHours: Record<string, string> = {};
    
    if (!hoursString) return formattedHours;
    
    let currentDay = "";
    let currentHours = "";
    let tempHours = hoursString;
    
    for (const day of days) {
      if (tempHours.includes(day)) {
        if (currentDay) {
          formattedHours[currentDay] = currentHours;
        }
        
        const dayIndex = tempHours.indexOf(day);
        tempHours = tempHours.substring(dayIndex + day.length);
        currentDay = day;
        
        // Extract hours until next day or end
        const nextDayIndex = days.some(d => tempHours.includes(d)) 
          ? Math.min(...days.filter(d => tempHours.includes(d)).map(d => tempHours.indexOf(d)))
          : tempHours.length;
        
        currentHours = tempHours.substring(0, nextDayIndex).trim();
      }
    }
    
    // Add the last day
    if (currentDay) {
      formattedHours[currentDay] = currentHours;
    }
    
    return formattedHours;
  };

  const hours = formatHours(restaurant.hours);

  return (
    <div className="min-h-screen bg-background">
      <header className="bg-primary text-primary-foreground py-6">
        <div className="container mx-auto px-4">
          <button 
            onClick={() => navigate("/")}
            className="flex items-center mb-4 hover:underline"
          >
            <ArrowLeft size={16} className="mr-1" />
            Retour à la liste
          </button>
          <div className="flex flex-col md:flex-row md:items-center md:justify-between">
            <div>
              <h1 className="text-3xl font-bold">{restaurant.name}</h1>
              <div className="flex items-center mt-2">
                <MapPin size={16} className="mr-1" />
                <span>{restaurant.address}</span>
              </div>
            </div>
            <div className="mt-4 md:mt-0 flex items-center bg-background text-primary px-3 py-2 rounded-full">
              <Star size={20} className="mr-1 fill-secondary text-secondary" />
              <span className="font-bold">{restaurant.rating}</span>
              <span className="text-sm ml-1 text-foreground opacity-75">({restaurant.reviews})</span>
            </div>
          </div>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <div className="bg-card shadow rounded-lg p-6 mb-8">
              <h2 className="text-xl font-bold mb-4 border-b pb-2">Informations</h2>
              
              {restaurant.phone && (
                <div className="mb-4">
                  <h3 className="font-semibold mb-1">Contact</h3>
                  <p>{restaurant.phone}</p>
                </div>
              )}
              
              <div className="mb-4">
                <h3 className="font-semibold mb-1">Horaires d'ouverture</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                  {Object.entries(hours).length > 0 ? (
                    Object.entries(hours).map(([day, time]) => (
                      <div key={day} className="flex justify-between">
                        <span>{day}</span>
                        <span>{time}</span>
                      </div>
                    ))
                  ) : (
                    <p>Horaires non disponibles</p>
                  )}
                </div>
              </div>
              
              {restaurant.service_options.length > 0 && (
                <div className="mb-4">
                  <h3 className="font-semibold mb-1">Services</h3>
                  <div className="flex flex-wrap gap-2">
                    {restaurant.service_options.map((option: string) => (
                      <span key={option} className="bg-muted px-2 py-1 rounded text-sm">
                        {option}
                      </span>
                    ))}
                  </div>
                </div>
              )}
              
              {restaurant.highlights.length > 0 && (
                <div className="mb-4">
                  <h3 className="font-semibold mb-1">Points forts</h3>
                  <div className="flex flex-wrap gap-2">
                    {restaurant.highlights.map((highlight: string) => (
                      <span key={highlight} className="bg-secondary/20 text-secondary-foreground px-2 py-1 rounded text-sm">
                        {highlight}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
            
            <div className="bg-card shadow rounded-lg p-6">
              <h2 className="text-xl font-bold mb-4 border-b pb-2">Caractéristiques</h2>
              
              {restaurant.offerings.length > 0 && (
                <div className="mb-4">
                  <h3 className="font-semibold mb-1">Offre</h3>
                  <div className="flex flex-wrap gap-2">
                    {restaurant.offerings.map((offer: string) => (
                      <span key={offer} className="bg-muted px-2 py-1 rounded text-sm">
                        {offer}
                      </span>
                    ))}
                  </div>
                </div>
              )}
              
              {restaurant.dining_options.length > 0 && (
                <div className="mb-4">
                  <h3 className="font-semibold mb-1">Options de repas</h3>
                  <div className="flex flex-wrap gap-2">
                    {restaurant.dining_options.map((option: string) => (
                      <span key={option} className="bg-muted px-2 py-1 rounded text-sm">
                        {option}
                      </span>
                    ))}
                  </div>
                </div>
              )}
              
              {restaurant.amenities.length > 0 && (
                <div className="mb-4">
                  <h3 className="font-semibold mb-1">Équipements</h3>
                  <div className="flex flex-wrap gap-2">
                    {restaurant.amenities.map((amenity: string) => (
                      <span key={amenity} className="bg-muted px-2 py-1 rounded text-sm">
                        {amenity}
                      </span>
                    ))}
                  </div>
                </div>
              )}
              
              {restaurant.atmosphere.length > 0 && (
                <div className="mb-4">
                  <h3 className="font-semibold mb-1">Ambiance</h3>
                  <div className="flex flex-wrap gap-2">
                    {restaurant.atmosphere.map((atmos: string) => (
                      <span key={atmos} className="bg-muted px-2 py-1 rounded text-sm">
                        {atmos}
                      </span>
                    ))}
                  </div>
                </div>
              )}
              
              {restaurant.crowd.length > 0 && (
                <div className="mb-4">
                  <h3 className="font-semibold mb-1">Clientèle</h3>
                  <div className="flex flex-wrap gap-2">
                    {restaurant.crowd.map((crowd: string) => (
                      <span key={crowd} className="bg-muted px-2 py-1 rounded text-sm">
                        {crowd}
                      </span>
                    ))}
                  </div>
                </div>
              )}
              
              {restaurant.children.length > 0 && (
                <div>
                  <h3 className="font-semibold mb-1">Enfants</h3>
                  <div className="flex flex-wrap gap-2">
                    {restaurant.children.map((childInfo: string) => (
                      <span key={childInfo} className="bg-muted px-2 py-1 rounded text-sm">
                        {childInfo}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
          
          <div className="lg:col-span-1">
            <div className="bg-card shadow rounded-lg p-6">
              <h2 className="text-xl font-bold mb-4">Localisation</h2>
              
              <Tabs defaultValue="map">
                <TabsList className="w-full mb-4">
                  <TabsTrigger value="map" className="flex-1">
                    <Map size={16} className="mr-2" />
                    Carte
                  </TabsTrigger>
                  <TabsTrigger value="3d" className="flex-1">
                    <span className="mr-2">3D</span>
                    Vue 3D
                  </TabsTrigger>
                </TabsList>
                <TabsContent value="map">
                  <RestaurantMap 
                    latitude={restaurant.latitude} 
                    longitude={restaurant.longitude}
                    name={restaurant.name}
                  />
                </TabsContent>
                <TabsContent value="3d">
                  <Restaurant3DView 
                    latitude={restaurant.latitude}
                    longitude={restaurant.longitude}
                  />
                </TabsContent>
              </Tabs>
            </div>
          </div>
        </div>
      </main>

      <footer className="bg-muted py-6">
        <div className="container mx-auto px-4 text-center text-muted-foreground">
          <p>© {new Date().getFullYear()} Guide des Restaurants Chinois à Antananarivo</p>
        </div>
      </footer>
    </div>
  );
};

export default RestaurantDetail;
