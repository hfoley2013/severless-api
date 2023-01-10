import pytest
import requests
from http.server import HTTPServer
from threading import Thread
from api.capital_finder import handler

def test_find_capital_by_country():
    # Test the handler class with a country name
    with HTTPServer(("", 8000), handler) as httpd:
        thread = Thread(target=httpd.serve_forever)
        thread.start()
        response = requests.get("http://localhost:8000/api/capital_finder?country=Chile")
        assert response.text == "The capital of Chile is Santiago."
        httpd.shutdown()

def test_find_capital_by_capital():
    # Test the handler(BaseHTTPRequestHandler) class with a capital name
    with HTTPServer(("", 8001), handler) as httpd:
        thread = Thread(target=httpd.serve_forever)
        thread.start()
        response = requests.get("http://localhost:8001/api/capital_finder?capital=Santiago")
        assert response.text == "Santiago is the capital of Chile."
        httpd.shutdown()

def test_find_capital_missing_parameter():
    # Test the handler class with no parameters
    with HTTPServer(("", 8002), handler) as httpd:
        thread = Thread(target=httpd.serve_forever)
        thread.start()
        response = requests.get("http://localhost:8002/api/capital_finder")
        assert response.text == "Give me a country or a capital to find."
        httpd.shutdown()
