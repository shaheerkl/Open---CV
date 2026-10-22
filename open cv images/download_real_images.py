from pathlib import Path
import requests

# Run this script on your computer with internet access.
# Install first: python -m pip install requests
OUT = Path(__file__).resolve().parent
PHOTOS = [
    ("01_car_sports.jpg", "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1200&q=85"),
    ("02_car_road.jpg", "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1200&q=85"),
    ("03_city_street.jpg", "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=1200&q=85"),
    ("04_traffic_street.jpg", "https://images.unsplash.com/photo-1519501025264-65ba15a82390?auto=format&fit=crop&w=1200&q=85"),
    ("05_mountain_view.jpg", "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=85"),
    ("06_forest.jpg", "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1200&q=85"),
    ("07_beach.jpg", "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=85"),
    ("08_waterfall.jpg", "https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?auto=format&fit=crop&w=1200&q=85"),
    ("09_flower.jpg", "https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=1200&q=85"),
    ("10_dog.jpg", "https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=1200&q=85"),
    ("11_cat.jpg", "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=1200&q=85"),
    ("12_bicycle.jpg", "https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=1200&q=85"),
    ("13_buildings.jpg", "https://images.unsplash.com/photo-1487958449943-2429e8be8625?auto=format&fit=crop&w=1200&q=85"),
    ("14_bridge.jpg", "https://images.unsplash.com/photo-1519608487953-e999c86e7455?auto=format&fit=crop&w=1200&q=85"),
    ("15_food.jpg", "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?auto=format&fit=crop&w=1200&q=85"),
    ("16_fruit.jpg", "https://images.unsplash.com/photo-1619566636858-adf3ef46400b?auto=format&fit=crop&w=1200&q=85"),
    ("17_person_portrait.jpg", "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=1200&q=85"),
    ("18_sunset.jpg", "https://images.unsplash.com/photo-1472120435266-53107fd0c44a?auto=format&fit=crop&w=1200&q=85"),
    ("19_snow_mountain.jpg", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=85"),
    ("20_road_landscape.jpg", "https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1200&q=85"),
]

success = 0
for name, url in PHOTOS:
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        if not r.headers.get("content-type", "").startswith("image/"):
            raise ValueError("URL did not return an image")
        (OUT / name).write_bytes(r.content)
        print("Downloaded:", name)
        success += 1
    except Exception as e:
        print("FAILED:", name, "-", e)
print(f"Downloaded {success} of {len(PHOTOS)} images into {OUT}")
