import random
from typing_extensions import Self


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.hp = health
        self.atk = attack

    def attack(self, target):
        chance = random.uniform(0, 1)
        if chance > target.eva:
            print(self.name + ' hit you.')
            return self.atk
        else:
            print(self.name + '\'s attack miss.')
            return 0


# FOR TESTING PURPOSES
# easy = Enemy('Slime', 50)
# normal = Enemy('Goblin', 100)
# hard = Enemy('Golem', 200)
# easy.attack()
# normal.attack()
# hard.attack()
