import requests
import pandas as pd
import matplotlib.pyplot as plt


api_key = "d5bfda5cb05ad0f015691cdce9c58b98"
base_url = "http://api.openweathermap.org/data/2.5/air_pollution"


cities = {
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "Boston": {"lat": 42.3601, "lon": -71.0589},
    "Miami": {"lat": 25.7617, "lon": -80.1918},
    "Washington DC": {"lat": 38.9072, "lon": -77.0369},
    "Philadelphia": {"lat": 39.9526, "lon": -75.1652},
    "Charlotte": {"lat": 35.2271, "lon": -80.8431},
    "Wilmington": {"lat": 34.2257, "lon": -77.9447}
}


def get_air_pollution_data(city_coordinates):
    response = requests.get(base_url, params={
        "lat": city_coordinates["lat"], 
        "lon": city_coordinates["lon"], 
        "appid": api_key
    })
    if response.status_code == 200:
        return response.json()
    else:
        return None


pollution_data = []
for city, coords in cities.items():
    data = get_air_pollution_data(coords)
    if data:
        co_value = data['list'][0]['components']['co'] 
        pollution_data.append({"City": city, "CO": co_value})


df = pd.DataFrame(pollution_data)

print(df)


plt.figure(figsize=(10,6))
plt.bar(df['City'], df['CO'], color='blue')
plt.xlabel('City')
plt.ylabel('CO (μg/m³)')
plt.title('Air Pollution (CO Levels) in Major East Coast Cities')
plt.xticks(rotation=45)
plt.show()
