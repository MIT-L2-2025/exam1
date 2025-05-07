
import { useNavigate } from "react-router-dom";

type RestaurantCardProps = {
  id: number;
  name: string;
  address: string;
  phone: string | null;
  rating: string;
};

const RestaurantCard = ({ id, name, address, phone, rating }: RestaurantCardProps) => {
  const navigate = useNavigate();

  const handleCardClick = () => {
    navigate(`/restaurant/${id}`);
  };

  return (
    <div 
      className="restaurant-card bg-card border border-border rounded-lg shadow-md overflow-hidden cursor-pointer hover:shadow-lg"
      onClick={handleCardClick}
    >
      <div className="p-6">
        <div className="flex justify-between items-start">
          <h3 className="text-xl font-bold text-primary mb-2">{name}</h3>
          <div className="bg-secondary text-secondary-foreground px-2 py-1 rounded-md text-sm font-medium">
            ★ {rating}
          </div>
        </div>
        <p className="text-sm text-muted-foreground mb-2">{address}</p>
        {phone && <p className="text-sm">{phone}</p>}
      </div>
    </div>
  );
};

export default RestaurantCard;
