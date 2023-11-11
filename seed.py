from functools import lru_cache
from typing import Union, Generator
import requests
from pysondb import getDb


class PokeAPI:
    @staticmethod
    @lru_cache
    def get_pokemon(name: Union[int, str]) -> dict:
        url: str = f'https://pokeapi.co/api/v2/pokemon/{name}'
        data: dict = requests.get(url).json()
        return data

    @staticmethod
    def get_all(get_full=False) -> Generator:
        url: str = 'https://pokeapi.co/api/v2/pokemon/'
        data: dict = requests.get(url).json()
        while True:
            for pokemon in data['results']:
                if get_full:
                    yield PokeAPI.get_pokemon(pokemon['name'])
                else:
                    yield dict(name=pokemon['name'])
            if data['next'] is None:
                break
            url = data['next']
            data = requests.get(url).json()


def main():
    pokemons_db = getDb('pokemons.json', '_id')
    data = []
    for i, pokemon in enumerate(PokeAPI.get_all(True)):
        # filtered_pokemon = {
        #     'id': pokemon['id'],
        #     'name': pokemon['name'],
        #     'base_experience': pokemon['base_experience'],
        #     'height': pokemon['height'],
        #     'weight': pokemon['weight'],
        #     'order': pokemon['order'],
        #     'stats': pokemon['stats'],
        #     'types': pokemon['types'],
        #     'sprites': pokemon['sprites'],
        #     'game_indices': pokemon['game_indices']
        # }
        print(pokemon['name'])
        data.append(pokemon)
        if i % 20 == 19:
            print('Saving...')
            pokemons_db.addMany(data)
            data.clear()

    print('Saving...')
    pokemons_db.addMany(data)
    data.clear()


if __name__ == '__main__':
    main()
