from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        print(query_string_list)
        
        if "capital" in dic:
            url = "https://restcountries.com/v2/capital/"
            r = requests.get(url + dic["capital"])
            data = r.json()
            definitions = []
            for country_info in data:
                definition = country_info["meanings"][0]["definitions"][0]["definition"]
                definitions.append(definition)
            message = str(definitions)

        else:
            message = "Give me a country and I will return the capital city, or give me a capital city and I will return its country."

        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.end_headers()

        self.wfile.write(message.encode())

        return

# if __name__ == '__main__':
#     handler(BaseHTTPRequestHandler)
