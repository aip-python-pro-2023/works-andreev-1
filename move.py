# Базовый (родительский) класс
class Move:
    def __init__(self, name, pp, priority, power):
        self._name = name
        self._pp = pp
        self._priority = priority
        self._power = power
        self._type = None

    def __str__(self):
        return f"Move(name={self._name}, pp={self._pp}, priority={self._priority}, power={self._power})"

    def get_damage(self, other_type):
        pass


# Дочерний класс 1
class NormalMove(Move):
    def __init__(self, name, pp, priority, power):
        super().__init__(name, pp, priority, power)
        self._type = 'normal'

    def __str__(self):
        return f"NormalMove(name={self._name}, pp={self._pp}, priority={self._priority}, power={self._power})"

    def get_damage(self, other_type):
        if other_type == 'rock' or other_type == 'steel':
            return 0.5 * self._power
        if other_type == 'ghost':
            return 0 * self._power
        return 1 * self._power


# Дочерний класс 2
class FireMove(Move):
    def __init__(self, name, pp, priority, power):
        super().__init__(name, pp, priority, power)
        self._type = 'fire'

    def get_damage(self, other_type):
        double_damage_types = ['grass', 'ice', 'bug', 'steel']
        half_damage_types = ['fire', 'water', 'rock', 'dragon']

        if other_type in double_damage_types:
            return 2 * self._power
        if other_type in half_damage_types:
            return 0.5 * self._power
        return 1 * self._power


fireball = FireMove('fireball', 40, 0, 65)
punch = NormalMove('punch', 10, 0, 30)

print(fireball)
print(punch)

print(fireball.get_damage('steel'))
print(punch.get_damage('steel'))


