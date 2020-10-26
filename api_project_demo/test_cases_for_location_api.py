import unittest, requests
from urllib.parse import urlencode
import configparser

# Initialize the configparser in order to get credentials from config.ini file
config = configparser.ConfigParser()
config.read('./config.ini')

# Global variables
api_key = config['Credentials']['GOOGLE_API_KEY']
place_id = config['Credentials']['PLACE_ID']
rapidapi_key = config['Credentials']['RAPIDAPI_KEY']
base_google_api_url = 'https://maps.googleapis.com/maps/api/'


class LocationApiTestCases(unittest.TestCase):

    # API Reference: https://developers.google.com/places/web-service/details
    # This test verifies name of a place is in the endpoint responce
    # using its placeid parameter
    def test_google_endpoint_place_details(self):
        detail_url = 'place/details/json'
        detail_base_endpoint = f'{base_google_api_url}{detail_url}'

        detail_params = {
            'placeid': place_id,
            'fields': 'name,rating,formatted_phone_number',
            'key': api_key
        }

        detail_params_encoded = urlencode(detail_params)

        geocoding_endpoint_url = f'{detail_base_endpoint}?{detail_params_encoded}'
        response = requests.get(geocoding_endpoint_url)

        self.assertEqual(200, response.status_code)
        self.assertIn('residencial villa bonita'.title(), response.json().get('result').get('name'))


    # API Reference: https://developers.google.com/maps/documentation/geocoding/overview
    # This test verifies that searching address string return valid results
    def test_google_geocoding_endpoint(self):
        geocoding_url = 'geocode/json'

        params = {
            'address': 'residencial villa bonita, cartago',
            'key': api_key
        }

        url_params = urlencode(params)
        geocoding_endpoint = f'{base_google_api_url}{geocoding_url}?{url_params}'

        response = requests.get(geocoding_endpoint)

        self.assertEqual(200, response.status_code)

        place_id_in_response = response.json().get('results')[0]['place_id']

        self.assertEqual(place_id, place_id_in_response)

    # API Reference: https://developers.google.com/places/web-service/details#PlaceDetailsStatusCodes
    # This test verifies the error message returned when API_KEY is wrong
    def test_google_error_message_with_incorrect_api_key(self):
        detail_url = 'place/details/json'
        detail_base_endpoint = f'{base_google_api_url}{detail_url}'

        detail_params = {
            'placeid': place_id,
            'fields': 'name,rating,formatted_phone_number',
            'key': api_key + 'wrong'
        }

        detail_params_encoded = urlencode(detail_params)
        geocoding_endpoint_url = f'{detail_base_endpoint}?{detail_params_encoded}'

        response = requests.get(geocoding_endpoint_url)

        self.assertEqual(200, response.status_code)
        self.assertEqual('The provided API key is invalid.', response.json()['error_message'])
        self.assertEqual('REQUEST_DENIED', response.json().get('status'))

    # API Reference: https://developers.google.com/maps/documentation/geocoding/overview#StatusCodes
    # This test case verifies that entering random string search parameter
    # return an error message
    def test_google_error_message_with_incorrect_search_address_parameter(self):
        geocoding_url = 'geocode/json'
        incorrect_address = 'sladlasdlas'

        params = {
            'address': incorrect_address,
            'key': api_key
        }

        url_params = urlencode(params)
        geocoding_endpoint = f'{base_google_api_url}{geocoding_url}?{url_params}'

        response = requests.get(geocoding_endpoint)

        self.assertEqual(200, response.status_code)
        self.assertEqual('ZERO_RESULTS', response.json().get('status'))

    # API Reference: https://developers.google.com/places/web-service/details#PlaceDetailsStatusCodes
    # This test case verifies the error when a required parameter is
    # not send in the payload i.e 'placeid'
    def test_google_error_message_missing_required_parameter(self):
        detail_url = 'place/details/json'
        detail_base_endpoint = f'{base_google_api_url}{detail_url}'

        detail_params = {
            'fields': 'name,rating,formatted_phone_number',
            'key': api_key
        }

        detail_params_encoded = urlencode(detail_params)
        geocoding_endpoint_url = f'{detail_base_endpoint}?{detail_params_encoded}'

        response = requests.get(geocoding_endpoint_url)

        self.assertEqual(200, response.status_code)
        self.assertEqual('Missing the placeid or reference parameter.', response.json().get('error_message'))
        self.assertEqual('INVALID_REQUEST', response.json().get('status'))

    # API Reference: https://wirefreethought.github.io/geodb-cities-api-docs/
    # This test case verifies 401 status code
    def test_401_unauthorized_error_message(self):
        incorrect_headers = {
            'Authorization': 'Bearer wrong_bearer_token',
            'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com'
        }
        response = requests.get('https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions?limit=5&offset=0',
                                headers=incorrect_headers)

        self.assertEqual(401, response.status_code)
        self.assertIn('Missing RapidAPI application key.', response.json()['message'])

    # API Reference: https://wirefreethought.github.io/geodb-cities-api-docs/
    # This test case verifies 400 status code
    def test_400_bad_request_error_message(self):
        headers = {
            'x-rapidapi-key': rapidapi_key,
            'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com'
        }

        url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions?radius=asas&limit=5&offset=0'

        response = requests.get(url, headers=headers)

        self.assertEqual(400, response.status_code)
        self.assertEqual('BAD_REQUEST', response.json().get('errors')[0].get('code'))
        self.assertEqual('Type mismatch.', response.json()['errors'][0]['message'])

    # API Reference: https://gorest.co.in/
    # This test case is an example an end to end test for an object
    # This object is created, then requested, then updated and finally deleted
    # so there are assertions for each scenario
    def test_post_get_put_delete_methods_for_object_using_api(self):
        header = {
            'Authorization': f"Bearer {config['Credentials']['BEARER_TOKEN']}"
        }

        payload = {
            'name': 'QAomar',
            'email': '1omarjo@test.com',
            'status': 'Active',
            'gender': 'Male'
        }

        response = requests.post('https://gorest.co.in/public-api/users', json=payload,
                                 headers=header)

        self.assertEqual(200, response.status_code)
        user_id = int(response.json().get('data').get('id'))

        response = requests.get(f'https://gorest.co.in/public-api/users/{user_id}', headers=header)
        self.assertEqual(200, response.status_code)

        update_payload = {
            'name': 'QAomarupdated',
            'email': 'test1@test.com',
            'status': 'Inactive'
        }

        response = requests.put(f'https://gorest.co.in/public-api/users/{user_id}', json=update_payload, headers=header)

        self.assertEqual(200, response.status_code)
        self.assertIn('QAomarupdated', response.json().get('data').values())

        response = requests.delete(f'https://gorest.co.in/public-api/users/{user_id}', headers=header)
        self.assertEqual(200, response.status_code)


