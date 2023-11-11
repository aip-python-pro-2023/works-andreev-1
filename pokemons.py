from pysondb import getDb


def get_pokemon(name):
    db = getDb('pokemons.json')
    return db.getBy({'name': name})[0]
