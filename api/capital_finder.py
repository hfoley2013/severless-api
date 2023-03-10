from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" or "capital" not in dic:
            message = "Give me a country or a capital to find."
                
        if "country" in dic:
            query_country = dic["country"]
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + query_country.lower())
            data = r.json()
            country = str(data[0]['name']['common'])
            capital = str(data[0]['capital'][0])
            message = f"The capital of {country.capitalize()} is {capital.capitalize()}."

        if "capital" in dic:
            query_capital = dic['capital']
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + query_capital.lower())
            data = r.json()
            country = str(data[0]['name']['common'])
            capital = str(data[0]['capital'][0])
            message = f"{capital.capitalize()} is the capital of {country.capitalize()}."

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return
