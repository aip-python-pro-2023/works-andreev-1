import pokemons


class Pokemon:
    # Статическое поле класса Pokemon
    current_id = 1

    # Конструктор
    def __init__(self, pokemon_type, species, name, health, attack, defense, speed, experience):
        self.id = Pokemon.current_id
        Pokemon.current_id += 1
        self.type = pokemon_type
        self.species = species
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.experience = experience

    def __str__(self):
        return f'Pokemon(id={self.id}, species={self.species}, type={self.type}, name={self.name})'

    def __eq__(self, other):
        return isinstance(other, Pokemon) and self.id == other.id

    def __contains__(self, item):
        for i in 1, 2, 3, 4, 5:
            if i == item:
                return True
        return False

    def fight(self, other: 'Pokemon'):
        if self.speed > other.speed:
            first, second = self, other
        else:
            first, second = other, self
        while first.health > 0 and second.health > 0:
            damage = max(first.attack - second.defense, 0)
            second.health -= damage
            first, second = second, first

        return self.health > 0

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
scorbunny.health = 500

scorbunny_clone = Pokemon('fire', 'scorbunny', 'Scorbunny', 100, 25, 15, 30, 0)
print(scorbunny == scorbunny_clone)

grookey = Pokemon('grass', 'grookey', 'Grookey', 80, 20, 20, 25, 0)
grookey.speed = 30

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
print(scorbunny.health, grookey.health)