# LAB - Class 16

## Project: Country Finder

## Author: Harper Foley

## Links and Resources

* [GitHub Repo](https://github.com/hfoley2013/severless-api)
* [Deployed Site](https://capital-finder-harper-foley.vercel.app/)

### Setup

* To set up this repo create a local repository on your machine
* Create a virtual environment for Python
  * `python3.11 -m venv .venv`
* Activate the venv file
  * `source .venv/bin/activate`
* Install `pytest` and `pytest-watch`
  * `pip install pytest pytest-watch`
* Use `git clone` to clone the repo to your local machine
  * `git clone https://github.com/hfoley2013/severless-api.git`
* Install Vercel CLI:
  `npm i -g vercel`
* Your repo is now ready to run the Capital Finder program

### How to initialize/run

* To initialize the program run `vercel dev`
  * This will begin running the program in a `localhost` and allow you to print outputs to the console
* Query types
  * By Country
    * The url will appear like the following: `http://localhost:8001/api/capital_finder?country={query}`
    * Example: `http://localhost:8001/api/capital_finder?country=Peru`
    * Returns: `The capital of Peru is Lima.`
  * By Capital
    * The url will appear like the following: `http://localhost:8001/api/capital_finder?captial={query}`
    * Example: `http://localhost:8001/api/capital_finder?capital=Lima`
    * Returns: `Lima is the capital of Peru.`
* To run the test scripts:
  * Run `pytest` in the CLI

### Tests

* How do you run tests?
  * Tests are conducted via `pytest`
  * You may need to specify the location of the tests as follows:
    * `pytest tests/test_capital_finder.py`
* Tests check for the following:
  * Given `country=Peru`
    * Returns `The capital of Peru is Lima.`
  * Given `captial=Lima`
    * Return `Lima is the capital of Peru.`
  * Given `nothing`
    * Return `Give me a country or a capital to find.`
