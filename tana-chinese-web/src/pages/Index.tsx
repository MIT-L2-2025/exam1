
import { useState, useEffect } from "react";
import RestaurantCard from "@/components/RestaurantCard";
import restaurantsData from "@/data/restaurants.json";

const Index = () => {
  const [restaurants, setRestaurants] = useState<any[]>([]);

  useEffect(() => {
    setRestaurants(restaurantsData);
  }, []);

  return (
    <div className="min-h-screen bg-background">
      <header className="bg-primary text-primary-foreground py-8">
        <div className="container mx-auto px-4">
          <h1 className="text-3xl md:text-4xl font-bold">Restaurants Chinois à Antananarivo</h1>
          <p className="mt-2 text-lg opacity-90">Découvrez les meilleurs restaurants chinois de la ville</p>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {restaurants.map((restaurant) => (
            <RestaurantCard
              key={restaurant.id}
              id={restaurant.id}
              name={restaurant.name}
              address={restaurant.address}
              phone={restaurant.phone}
              rating={restaurant.rating}
            />
          ))}
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

export default Index;
