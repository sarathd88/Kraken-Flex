# Kraken-Flex
KrakenFlex Back End Test
API Outage Management System
This is a Python program that interacts with an API to manage outages. The program reads an API Swagger specification file, loads API key and URL from a config file, retrieves outages from the API, filters out outages that began before a specific date or don't have an ID that is in the list of devices in the site information, and sends the filtered and formatted outages back to the API.

The program also includes tests to verify the API response status code, response format, and actual data rows based on the API response.

Dependencies
This program requires the following dependencies:

requests
PyYAML
configparser
pytest
You can install these dependencies by running:

pip install -r requirements.txt
How to Run the Program
Clone this repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Set up the API URL and API key by modifying the config.ini file.
Run the program by executing python main.py.
How to Run the Tests
Ensure that the program and its dependencies are installed.
Run the tests by executing pytest in the terminal.
You can also run a specific test by executing pytest test_kraken.py
requirements.txt:

requests
PyYAML
pandas
configparser
pytest
