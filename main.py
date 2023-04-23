import requests
import yaml
import time
import configparser

# Load Swagger specification from file
with open('api.yaml') as file:
    spec = yaml.safe_load(file)
    # print(spec)
# Set up API URL and API key
# api_url = 'https://api.krakenflex.systems/interview-tests-mock-api/v1'
api_url = spec['servers'][0]['url']

# Read API key from config file
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['api']['key']


# Define function to make authenticated HTTP requests
def make_request(method, path, params=None, json=None):
    headers = {'x-api-key': api_key}
    url = api_url + path
    response = requests.request(method, url, headers=headers, params=params, json=json)
    response.raise_for_status()
    #print(f'Response status code: {response.status_code}')
    return response.json()


max_retries = 5
retry_count = 0
while retry_count < max_retries:
    try:
        # Retrieve all outages from the API
        # outages = make_request('GET', '/outages')
        outages = make_request('GET', list(spec['paths'].keys())[0])

        #print(outages)
        # Retrieve site information for the 'norwich-pear-tree' site
        # site_id_get = input("Enter the site ID: ")
        # site_info = make_request('GET', f'/site-info/{site_id_get}')
        site_info = make_request('GET', '/site-info/norwich-pear-tree')

        # Filter out outages that began before '2022-01-01T00:00:00.000Z' or don't have an ID that is in the list of devices in the site information
        filtered_outages = []
        for outage in outages:
            if outage['begin'] >= '2022-01-01T00:00:00.000Z' and outage['id'] in [device['id'] for device in
                                                                                  site_info['devices']]:
                filtered_outages.append({
                    'id': outage['id'],
                    'name': next((device['name'] for device in site_info['devices'] if device['id'] == outage['id']),
                                 None),
                    'begin': outage['begin'],
                    'end': outage['end']
                })

        # Send filtered and formatted outages to the API
        # site_id_post = input('Enter the post site ID: ')
        # make_request('POST', f'/site-outages/{site_id_post}', json=filtered_outages)
        make_request('POST', '/site-outages/norwich-pear-tree', json=filtered_outages)

        break  # Exit the loop if the request is successful
    except requests.exceptions.HTTPError as e:
        print(f'Error {e.response.status_code}: {e.response.reason}')
        if e.response.status_code == 500:
            print(f'Retrying in 5 seconds...')
            time.sleep(5)  # Wait for 5 seconds before retrying
        retry_count += 1
else:
    print("Maximum number of retries reached. Exiting...")



