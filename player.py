from pysondb import getDb


class Player:
    def __init__(self, player_id, nickname):
        self.__player_id = player_id
        self.__name = nickname
        self.__experience = 0
        self.__money = 0
        self.__pokemons = []

    @property
    def id(self):
        return self.__player_id

    @property
    def description(self):
        return f"""
*Тренер {self.__name}*

*Очки опыта*: {self.__experience} XP
*Деньги*: {self.__money} PC
*Покемоны*: {', '.join(pokemon['name'].capitalize() for pokemon in self.__pokemons)}
"""

    def as_dict(self):
        return {
            'player_id': self.__player_id,
            'name': self.__name,
            'experience': self.__experience,
            'money': self.__money,
            'pokemons': self.__pokemons
        }


class PlayerJSONRepository:
    __internal_id_field = '_id'

    def __init__(self, path):
        self.__path = path
        self.__primary_key = 'player_id'

    def get_all(self):
        db = getDb(self.__path, self.__internal_id_field)
        result = db.getAll()

        return result

    def get_one(self, player_id):
        db = getDb(self.__path, self.__internal_id_field)
        result = db.getByQuery({self.__primary_key: player_id})
        if not result:
            return None

        return result[0]

    def create(self, player):
        db = getDb(self.__path, self.__internal_id_field)

        result = db.getByQuery({self.__primary_key: player.id})
        if result:
            return False

        db.add(player.as_dict())
        return True
