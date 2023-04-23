#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pytest
import requests
import json
import yaml
import pandas as pd
import configparser

# Load Swagger specification from file
with open('api.yaml') as file:
    spec = yaml.safe_load(file)

# Set up API URL and API key
api_url = spec['servers'][0]['url']
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['api']['key']

# Define fixture to set up the API headers
@pytest.fixture
def api_headers():
    headers = {'x-api-key': api_key}
    return headers

# Define test function to test API response status code
def test_api_response_status(api_headers):
    url = api_url + "/outages"
    response = requests.get(url, headers=api_headers)
    assert response.status_code == 200

# Define test function to test API response format
def test_api_response_format(api_headers):
    url = api_url + "/outages"
    response = requests.get(url, headers=api_headers)
    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) > 0
    assert all('id' in item and 'begin' in item and 'end' in item for item in response_json)
# Define test function to test actual data rows based on the API response
def test_actual_data_rows(api_headers):
    url = api_url + "/outages"
    response = requests.get(url, headers=api_headers)
    response_json = response.json()
    df = pd.json_normalize(response_json)
    assert len(df) == len(response_json)
# Define test function to test API response status code for site-info GET request
def test_site_info_response_status(api_headers):
    url = api_url + "/site-info/norwich-pear-tree"
    response = requests.get(url, headers=api_headers)
    assert response.status_code == 200

# Define test function to test API response format for site-info GET request
def test_site_info_response_format(api_headers):
    url = api_url + "/site-info/norwich-pear-tree"
    response = requests.get(url, headers=api_headers)
    response_json = response.json()
    assert 'name' in response_json and 'devices' in response_json
    assert isinstance(response_json['devices'], list)
    assert all('id' in item and 'name' in item for item in response_json['devices'])

# In[ ]:




