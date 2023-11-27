class Pokemon:
    # Конструктор
    def __init__(self, pokemon_id, pokemon_type, species, name, health, attack, defense, speed, experience):
        self.id = pokemon_id
        self.type = pokemon_type
        self.species = species
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.experience = experience

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


# Вызов конструктора класса Pokemon
scorbunny = Pokemon(1, 'fire', 'scorbunny', 'Scorbunny', 100, 25, 15, 30, 0)
scorbunny.health = 500

grookey = Pokemon(2, 'grass', 'grookey', 'Grookey', 80, 20, 20, 25, 0)
grookey.speed = 30

result = scorbunny.fight(grookey)
print(result)
print(scorbunny.health, grookey.health)