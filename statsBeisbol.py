import requests

# URL para juegos del 4 de julio de 2023
url = "https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=2023-07-04"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # Explorar datos
    for game in data.get("dates", [])[0].get("games", []):
        print(f"Juego: {game['teams']['away']['team']['name']} vs {game['teams']['home']['team']['name']}")
        print(f"Hora: {game['gameDate']}")
    
else:
    print(f"Error: {response.status_code}")
