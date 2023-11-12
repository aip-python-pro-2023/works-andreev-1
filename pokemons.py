import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ['POKEAPI_BASE_URL']


def get_pokemon(name):
    result = requests.get(BASE_URL + f'/pokemon/{name}')
    return result.json() if result.ok else None
