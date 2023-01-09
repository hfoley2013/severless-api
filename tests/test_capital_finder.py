import pytest
from "../api/capital_finder.py" import *

def test_find_capital_by_country():
    # Test the handler class with a country name
    with HTTPServer(("", 8000), handler) as httpd:
        thread = Thread(target=httpd.serve_forever)
        thread.start()
        response = requests.get("http://localhost:8000/capital-finder?country=Chile")
        assert response.text == "The capital of Chile is Santiago."
        httpd.shutdown()

def test_find_capital_by_capital():
    # Test the handler class with a capital name
    with HTTPServer(("", 8000), handler) as httpd:
        thread = Thread(target=httpd.serve_forever)
        thread.start()
        response = requests.get("http://localhost:8000/capital-finder?capital=Santiago")
        assert response.text == "The capital of Chile is Santiago."
        httpd.shutdown()

def test_find_capital_missing_parameter():
    # Test the handler class with no parameters
    with HTTPServer(("", 8000), handler) as httpd:
        thread = Thread(target=httpd.serve_forever)
        thread.start()
        response = requests.get("http://localhost:8000/capital-finder")
        assert response.text == "Give me a country or a capital to find."
        httpd.shutdown()
