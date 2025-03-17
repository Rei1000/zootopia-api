import requests

API_KEY = "D8tjZCwFnSWBxSiTcqomLg==SacsubYILq9gVS5A"
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def check_connection():
    """ Testet, ob die API mit einem Beispiel-Tiernamen funktioniert """
    headers = {"X-Api-Key": API_KEY}
    url = f"{BASE_URL}?name=fox"  # 🔹 Hier fügen wir den name-Parameter hinzu!

    print(f"🔍 Debug: Anfrage an API → {url}")
    response = requests.get(url, headers=headers)

    print(f"🔍 Debug: API-Statuscode → {response.status_code}")
    print(f"Antwort: {response.text}")


check_connection()