import requests

def find_capital(request):
    # Parse the query string
    query_params = request.args
    if "country" in query_params:
        # Make a GET request to the REST Countries API with the given country name
        response = requests.get(f"https://restcountries.eu/v2/name/{query_params['country']}?fullText=true")
        data = response.json()
        # Return the capital of the country
        return f"The capital of {query_params['country']} is {data[0]['capital']}.", 200
    elif "capital" in query_params:
        # Make a GET request to the REST Countries API with the given capital name
        response = requests.get(f"https://restcountries.eu/v2/capital/{query_params['capital']}")
        data = response.json()
        # Return the name of the country with the given capital
        return f"{query_params['capital']} is the capital of {data[0]['name']['common']}.", 200
    else:
        return "Please provide a country or capital name.", 400
