import requests

def actueelWeer():
    url = "https://api.open-meteo.com/v1/forecast?latitude=51.83167&longitude=4.6875&current=temperature_2m"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            gegevens = response.json()
            temperatuur = gegevens["current"]["temperature_2m"]

            print(f"De actuele temperatuur in Papendrecht is {temperatuur} graden Celsius.")
        else:
            print("Weergegevens konden niet worden opgehaald.")

    except (requests.exceptions.RequestException, KeyError, ValueError, TypeError):
        print("Er is iets misgegaan bij het ophalen van de weergegevens.")
