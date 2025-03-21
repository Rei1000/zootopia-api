import json
import requests
import sys

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


def load_data(file_path):
    """Loads data from a JSON file and returns it."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Creates HTML for each animal."""
    card_title = f'<div class="card__title">{animal["name"].upper()}</div>'
    card_text = "<p class='card__text'>"

    if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
            diet = animal["characteristics"]["diet"]
            card_text += f"<strong>Diet:</strong> {diet}<br/>"

    if "locations" in animal and len(animal["locations"]) > 0:
        location = animal["locations"][0]
        card_text += f"<strong>Location:</strong> {location}<br/>"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        animal_type = animal["characteristics"]["type"]
        card_text += f"<strong>Type:</strong> {animal_type}<br/>"

    card_text += "</p>"
    full_card = f'<li class="cards__item">\n{card_title}\n{card_text}\n</li>'

    return full_card


def generate_animal_info(file_path):
    """Loads data from file and creates HTML for each animal."""
    animals = load_data(file_path)
    output_list = [serialize_animal(animal) for animal in animals]

    full_html = "<ul class='cards'>\n" + "\n".join(output_list) + "\n</ul>"
    return full_html


def load_template(template_file):
    """Reads an HTML file and returns its content."""
    with open(template_file, "r", encoding="utf-8") as file:
        return file.read()


def replace_placeholder(template, animal_html):
    """Replaces the placeholder in the template with animal HTML data."""
    return template.replace("__REPLACE_ANIMALS_INFO__", animal_html)


def save_html(filename, content):
    """Saves an HTML file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    while True:
        animal_name = input("Enter the name of the animal you want to search for (or type 'q' to quit): ").strip()

        if animal_name.lower() == "q":
            print("Exiting program.")
            sys.exit()

        if not animal_name:
            print("Error: Please enter a valid animal name.")
            continue

        data = fetch_animal_data(animal_name)
        if data:
            save_to_json(data)

            # Generate and update HTML file
            print("Generating updated animals.html file...")
            animal_html = generate_animal_info("animals_data.json")
            html_content = load_template("animals_template.html")
            html_content = replace_placeholder(html_content, animal_html)
            save_html("animals.html", html_content)

            print("Update completed! Open animals.html in your browser.")
            break
        else:
            print(f"Error: No data found for '{animal_name}'. Please try searching for another animal or type 'q' to exit.")
