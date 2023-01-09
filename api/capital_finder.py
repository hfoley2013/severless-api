from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["country"])
            data = r.json()
            country = dic['country']
            capital = str(data[0]['capital'][0])
            message = f"The capital of {country.capitalize()} is {capital.capitalize()}"

        elif "capital" in dic:
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + dic['capital'])
            data = r.json
            capital = dic['capital']
            country = str(data[0]['name']['common'][0])
            message = f"The capital of {country.capitalize()} is {capital.capitalize()}."
        
        else:
            message = "Give me a country or a capital to find."

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
