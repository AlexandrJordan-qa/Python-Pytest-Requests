
import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = "________________"

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 4065})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 4065})
    assert response.json()["trainer_name"] == "prod"
