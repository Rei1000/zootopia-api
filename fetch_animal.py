import requests
import json
import sys
import subprocess

# API Configuration
API_KEY = "D8tjZCwFnSWBxSiTcqomLg==SacsubYILq9gVS5A"
BASE_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_animal_data(animal_name):
    """
    Fetches animal data from the API based on the given animal name.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        list or None: A list of animal data if found, otherwise None.
    """
    headers = {"X-Api-Key": API_KEY}
    url = f"{BASE_URL}?name={animal_name}"

    print(f"Debug: Sending request to API → {url}")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if not data:
            print(f"Warning: No data found for '{animal_name}'.")
            return None
        return data
    else:
        print(f"Error: API request failed with status code {response.status_code}, {response.text}")
        return None

def save_to_json(data, filename="animals_data.json"):
    """
    Saves the fetched animal data to a JSON file.

    Args:
        data (list): The list of animal data to save.
        filename (str, optional): The name of the JSON file. Defaults to "animals_data.json".
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved in {filename}")

def generate_html():
    """
    Executes animals_web_generator.py to generate the updated HTML file.
    """
    print("Generating updated animals.html file...")
    try:
        subprocess.run([sys.executable, "animals_web_generator.py"], check=True)
        print("Update completed! Open animals.html in your browser.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to generate HTML file. {e}")

if __name__ == "__main__":
    animal_name = input("Enter the name of the animal you want to search for: ").strip()

    if not animal_name:
        print("Error: Please enter a valid animal name.")
    else:
        data = fetch_animal_data(animal_name)
        if data:
            save_to_json(data)
            generate_html()
        else:
            print(f"Error: No data found for '{animal_name}'. Please try searching for another animal.")