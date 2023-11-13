from pysondb import getDb
import pokemons


def register(player_id):
    db = getDb('players.json', '_id')

    result = db.getByQuery({'player_id': player_id})
    if result:
        return False

    db.add({
        'player_id': player_id,
        'experience': 0,
        'money': 0,
        'pokemons': [],
    })
    return True


def get_player(player_id):
    db = getDb('players.json', '_id')
    result = db.getByQuery({'player_id': player_id})
    if not result:
        return None

    return result[0]


def get_text_description(player_id):
    player = get_player(player_id)
    if player is None:
        return None

    return f"""
*Очки опыта*: {player['experience']} XP
*Деньги*: {player['money']} PC
*Покемоны*: {', '.join(pokemon['name'].capitalize() for pokemon in player['pokemons'])}
"""


def add_pokemon(player_id, pokemon_name):
    pokemon = pokemons.get_pokemon(pokemon_name)
    if pokemon is None:
        return False

    db = getDb('players.json', '_id')
    player = db.getByQuery({'player_id': player_id})[0]
    player['pokemons'].append({
        'name': pokemon_name,
        'experience': 0,
        'stats': {
            'hp': pokemon['stats'][0]['base_stat'],
            'attack': pokemon['stats'][1]['base_stat'],
            'defense': pokemon['stats'][2]['base_stat'],
            'special-attack': pokemon['stats'][3]['base_stat'],
            'special-defense': pokemon['stats'][4]['base_stat'],
            'speed': pokemon['stats'][5]['base_stat'],
        }
    })
    db.updateByQuery({'player_id': player_id}, player)
    return True
