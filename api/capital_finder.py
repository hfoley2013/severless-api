import http.server
import requests

class CapitalFinderHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query string
        query_params = parse_qs(urlparse(self.path).query)

        if "country" in query_params:
            # Make a GET request to the REST Countries API with the given country name
            response = requests.get(f"https://restcountries.eu/v2/name/{query_params['country'][0]}")
            data = response.json()
            # Return the capital of the country
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"The capital of {query_params['country'][0]} is {data[0]['capital']}.".encode())
        
        elif "capital" in query_params:
            # Make a GET request to the REST Countries API with the given capital name
            response = requests.get(f"https://restcountries.eu/v2/capital/{query_params['capital'][0]}")
            data = response.json()
            # Return the name of the country with the given capital
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"{query_params['capital'][0]} is the capital of {data[0]['name']['common']}.".encode())
        
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Please provide a country or capital name.".encode())

def handler(req):
    CapitalFinderHandler(req.headers, req.write, req.finish)
