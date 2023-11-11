from pysondb import getDb


def get_pokemon(name):
    db = getDb('pokemons.json')
    result = db.getBy({'name': name})
    return result[0] if result else None
