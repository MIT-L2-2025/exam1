
import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

// Fix for default marker icons in Leaflet with webpack/vite
// This is needed because Leaflet's default marker icons reference assets that aren't properly bundled
const icon = L.icon({
  iconUrl: "https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png",
  iconRetinaUrl: "https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon-2x.png",
  shadowUrl: "https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

type RestaurantMapProps = {
  latitude: number | null;
  longitude: number | null;
  name: string;
};

const RestaurantMap = ({ latitude, longitude, name }: RestaurantMapProps) => {
  if (!latitude || !longitude) {
    return (
      <div className="bg-muted p-6 rounded-lg text-center">
        <p>Aucune coordonnée disponible pour ce restaurant</p>
      </div>
    );
  }
  
  const position: [number, number] = [latitude, longitude];

  // Style for the map container
  const mapStyle = {
    height: '400px',
    width: '100%',
    borderRadius: '0.5rem'
  };

  return (
    <div className="space-y-4">
      <MapContainer 
        center={position} 
        zoom={14} 
        style={mapStyle}
        scrollWheelZoom={false}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Marker position={position} icon={icon}>
          <Popup>
            <strong>{name}</strong>
          </Popup>
        </Marker>
      </MapContainer>
    </div>
  );
};

export default RestaurantMap;
