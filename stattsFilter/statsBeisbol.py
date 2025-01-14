import requests
import os
import json

url = "https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=2023-07-04"
backup_file = "mlb_schedule_backup.json"

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()

        with open(backup_file, "w") as backup:
            json.dump(data, backup, indent=4)

        print("Datos obtenidos de la API:")
    else:
        print(f"Advertencia: La API no respondió correctamente. Código de estado: {response.status_code}")
        raise Exception("Fallo en la API")
except Exception as e:
    for i in range(10):
        print(f"Advertencia: Usando el archivo de respaldo debido a un error: {e}")

    if os.path.exists(backup_file):
        with open(backup_file, "r") as backup:
            data = json.load(backup)
            print("Datos cargados del archivo de respaldo:")
    else:
        print("Error: No hay un archivo de respaldo disponible.")
        data = {}

if data:
    games = data.get("dates", [])[0].get("games", [])

    winners = list(filter(lambda game: game["teams"]["away"].get("isWinner", False), games))

    for game in winners:
        print(f"Ganador: {game['teams']['away']['team']['name']} (Visitante)")
        print(f"Venció a: {game['teams']['home']['team']['name']} (Local)")
        print(f"Hora del juego: {game['gameDate']}")
