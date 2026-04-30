import requests

url = "https://api.openweathermap.org/data/2.5/"
api = "apicode"

def get_data():
    while True:
        try:
            city = input("Choose a city: ")
            site = requests.get(f"{url}weather?q={city}&appid={api}")
            site.raise_for_status()
            data = site.json()
            site.raise_for_status()
            return data
        except requests.exceptions.HTTPError:
            print("\nEnter the name correctly")
            continue
data = get_data()

print(f"\nLocation: {data["sys"]["country"]} , {data["name"]}")
print(f"Weather: {data["main"]["temp"]-273.15:.1f} celsius and {data["weather"][0]["description"]}")
print(f"Wind: {data["wind"]["speed"]} km/h")
print(f"Humidity: {data["main"]["humidity"]}%")
print(f"Visibility: {data["visibility"]/1000}km")
