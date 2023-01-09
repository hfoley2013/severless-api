import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/capital-finder")
def find_capital(country: str = None, capital: str = None):
    if country:
        # Make a GET request to the REST Countries API with the given country name
        response = requests.get(f"https://restcountries.eu/v2/name/{country}?fullText=true")
        data = response.json()
        # Return the capital of the country
        return f"The capital of {country} is {data[0]['capital']}."
    elif capital:
        # Make a GET request to the REST Countries API with the given capital name
        response = requests.get(f"https://restcountries.eu/v2/capital/{capital}")
        data = response.json()
        # Return the name of the country with the given capital
        return f"{capital} is the capital of {data[0]['name']['common']}."
    else:
        return "Please provide a country or capital name."
