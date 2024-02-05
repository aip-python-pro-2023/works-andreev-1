import pokemons


class Pokemon:
    # Статическое поле класса Pokemon
    current_id = 1
    __id: int
    __type: str
    __species: str
    __name: str
    __health: int
    __attack: int
    __defense: int
    __speed: int
    __experience: int

    # Конструктор
    def __init__(self,
                 pokemon_type: str,
                 species: str,
                 name: str,
                 health: int,
                 attack: int,
                 defense: int,
                 speed: int,
                 experience: int) -> None:
        self.__id = Pokemon.current_id
        Pokemon.current_id += 1
        self.__type = pokemon_type
        self.__species = species
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defense = defense
        self.__speed = speed
        self.__experience = experience

    # Геттер
    def get_experience(self):
        return self.__experience

    # Сеттер
    def set_experience(self, new_experience: int) -> None:
        if 0 <= new_experience - self.__experience <= 1000:
            self.__experience = new_experience

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        if 0 <= value - self.__experience <= 1000:
            self.__experience = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        bad_words = ['Дурак']
        if value not in bad_words:
            self.__name = value

    def __str__(self):
        return f'Pokemon(id={self.__id}, species={self.__species}, type={self.__type}, name={self.__name}, experience={self.__experience})'

    def __eq__(self, other):
        return isinstance(other, Pokemon) and self.__id == other.__id

    def __contains__(self, item):
        for i in 1, 2, 3, 4, 5:
            if i == item:
                return True
        return False

    def fight(self, other: 'Pokemon'):
        if self.__speed > other.__speed:
            first, second = self, other
        else:
            first, second = other, self
        while first.__health > 0 and second.__health > 0:
            damage = max(first.__attack - second.__defense, 0)
            second.__health -= damage
            first, second = second, first

        return self.__health > 0

    @staticmethod
    def create_from_species(species, name):
        data = pokemons.get_pokemon(species)
        return Pokemon(
            pokemon_type=[t['type']['name'] for t in data['types']],
            species=species,
            name=name,
            health=data['stats'][0]['base_stat'],
            attack=data['stats'][1]['base_stat'],
            defense=data['stats'][2]['base_stat'],
            speed=data['stats'][5]['base_stat'],
            experience=0,
        )


# Вызов конструктора класса Pokemon
scorbunny = Pokemon('fire', 'scorbunny', 'Scorbunny', 100, 25, 15, 30, 0)
# scorbunny.__health = 500
# scorbunny.__experience = 100_000

scorbunny_clone = Pokemon('fire', 'scorbunny', 'Scorbunny', 100, 25, 15, 30, 0)
print(scorbunny == scorbunny_clone)

grookey = Pokemon('grass', 'grookey', 'Grookey', 80, 20, 20, 25, 0)
# grookey.__speed = 30

bulbasaur = Pokemon.create_from_species('bulbasaur', 'Bulbasaur')

print(scorbunny)
print(scorbunny_clone)
print(grookey)
print(bulbasaur)

# Вот так лучше не делать
# print(scorbunny.current_id)
# scorbunny.current_id += 1

# Pokemon.current_id += 1

result = scorbunny.fight(grookey)
print(result)
# print(scorbunny.__health, grookey.__health)
print(scorbunny.get_experience())

# Используем геттер и сеттер
scorbunny.set_experience(scorbunny.get_experience() + 100)
# Используем свойство
scorbunny.experience += 100

scorbunny.name = 'Test'
