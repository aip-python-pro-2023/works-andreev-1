import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ['POKEAPI_BASE_URL']


def get_pokemon(name):
    result = requests.get(BASE_URL + f'/pokemon/{name}')
    return result.json() if result.ok else None


def get_text_description(name):
    pokemon = get_pokemon(name)
    if pokemon is None:
        return None
    return f"""*Название*: {pokemon['name']}
*Рост*: {pokemon['height'] * 10} см
*Вес*: {pokemon['weight'] * 100} г
*Типы*: {', '.join([t['type']['name'].capitalize() for t in pokemon['types']])}

*Базовое здоровье*: {pokemon['stats'][0]['base_stat']}
*Базовая сила атаки*: {pokemon['stats'][1]['base_stat']}
*Базовая защита*: {pokemon['stats'][2]['base_stat']}
*Базовая сила спецатаки*: {pokemon['stats'][3]['base_stat']}
*Базовая спецзащита*: {pokemon['stats'][4]['base_stat']}
*Скорость*: {pokemon['stats'][5]['base_stat']}
"""
