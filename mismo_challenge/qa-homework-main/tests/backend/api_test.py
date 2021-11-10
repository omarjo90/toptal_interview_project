import json
import requests

base_url = 'http://127.0.0.1:5000/api'


def test_get_cells():
    response = requests.get(f'{base_url}/cells')
    # print(json.dumps(response.json()[8], indent=4))
    assert response.status_code == 200
    # print(response.json()[8].get('value'))
    assert response.json()[8].get('value') is None


def test_update_cell_value():
    payload = {
        'value': '=A1+A2'
    }

    response = requests.put(f'{base_url}/cell/A_5/', json=payload)
    # print(json.dumps(response.json(), indent=4))
    assert response.status_code == 200
    assert response.json()[0].get('value') == '=A1+A2'
    assert response.json()[0].get('row') == 5


def test_cell_updates_correctly():
    payload = {
        'value': '7'
    }

    response1 = requests.put(f'{base_url}/cell/A_1/', json=payload)
    assert response1.status_code == 200

    payload = {
        'value': '3'
    }

    response2 = requests.put(f'{base_url}/cell/A_2/', json=payload)
    assert response2.status_code == 200

    payload = {
        'value': '=A1+A2'
    }

    response3 = requests.put(f'{base_url}/cell/A_3/', json=payload)
    assert response3.status_code == 200
    assert response3.json()[0].get('computed') == 10




