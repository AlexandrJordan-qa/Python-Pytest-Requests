import requests
import pytest

BASE_URL = 'https://api.pokemonbattle.me:9104'
TRAINER_ID = '3952'

@pytest.fixture
def headers():
    trainer_token = 'd5b77261359b0086d523dee1a3a26d0c'
    return {
        'Content-Type': 'application/json',
        'trainer_token': trainer_token
    }

def test_get_trainers_status_code():
    response = requests.get(f'{BASE_URL}/trainers', params={'id': TRAINER_ID})
    assert response.status_code == 200, f'Expected 200, but got {response.status_code}'

def test_get_trainers_contains_expected_trainer_name(headers):
    response = requests.get(f'{BASE_URL}/trainers', params={'id': TRAINER_ID}, headers=headers)
    assert response.status_code == 200, f'Expected 200, but got {response.status_code}'
    
    trainers_list = response.json()
    assert isinstance(trainers_list, list), 'Expected a list in response'

    # Проверяем, что в списке есть хотя бы один тренер и имя этого тренера совпадает с ожидаемым
    trainer_with_expected_name = next((trainer for trainer in trainers_list if trainer.get('name') == 'AlexaJordan'), None)
    assert trainer_with_expected_name is not None, 'Trainer with expected name not found'
    assert trainer_with_expected_name.get('id') == int(TRAINER_ID), f'Trainer ID does not match expected value {TRAINER_ID}'
