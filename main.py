import requests

BASE_URL = 'https://api.pokemonbattle.me:9104'

def send_post_request(endpoint, data=None, headers=None, timeout=5):
    url = f'{BASE_URL}{endpoint}'
    response = requests.post(url=url, json=data, headers=headers, timeout=timeout)
    return response

def send_put_request(endpoint, data=None, headers=None, timeout=5):
    url = f'{BASE_URL}{endpoint}'
    response = requests.put(url=url, json=data, headers=headers, timeout=timeout)
    return response

def main():
    trainer_token = "d5b77261359b0086d523dee1a3a26d0c"

    headers = {
        'Content-Type': 'application/json',
        'trainer_token': trainer_token
    }

    pokemon_data = {
        "name": "generate",
        "photo": "generate"
    }

    # Создание покемона
    response_create_pokemon = send_post_request('/pokemons', data=pokemon_data, headers=headers)
    
    print(f'Create Pokemon: Code: {response_create_pokemon.status_code} - {response_create_pokemon.reason}. Message: {response_create_pokemon.text}')

    if response_create_pokemon.status_code == 201:
        pokemon_id = response_create_pokemon.json().get('id')
        print(f'Pokemon ID: {pokemon_id}')

        # Изменение имени покемона
        new_name_data = {
            "pokemon_id": pokemon_id,
            "name": "New Name",
            "photo": "https://dolnikov.ru/pokemons/albums/008.png"
        }

        response_change_name = send_put_request('/pokemons', data=new_name_data, headers=headers)

        print(f'Change Pokemon Name: Code: {response_change_name.status_code} - {response_change_name.reason}. Message: {response_change_name.text}')

        if response_change_name.status_code == 200:
            print('Name Changed Successfully!')

            # Поймать покемона в покебол
            catch_pokemon_data = {
                "pokemon_id": str(pokemon_id)
            }

            response_catch_pokemon = send_post_request('/trainers/add_pokeball', data=catch_pokemon_data, headers=headers)

            print(f'Catch Pokemon: Code: {response_catch_pokemon.status_code} - {response_catch_pokemon.reason}. Message: {response_catch_pokemon.text}')

            if response_catch_pokemon.status_code == 200:
                print('Pokemon Caught Successfully!')
            else:
                print('Failed to Catch Pokemon!')

        else:
            print('Failed to Change Name!')

    else:
        print('Failed to Create Pokemon!')

if __name__ == "__main__":
    main()
