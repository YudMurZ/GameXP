import random
import time
from os import system
from character import Player


class Enemy:
    def __init__(self, data: list):
        self.name = data[0]
        self.hp = self.max_hp = data[1]
        self.atk = data[2]

    def receiveDmg(self, dmg):
        self.hp -= dmg
        print(f'{self.name} received {dmg} damage.')
        time.sleep(2)
        if self.hp <= 0:
            print(self.name + ' is dead.')
            return 'enemy die'

    def attack(self, target: Player):
        system('cls')
        if random.uniform(0, 1) >= target.eva/100:
            print(self.name + ' hit you.')
            target.receiveDmg(self.atk)
        else:
            print(self.name + '\'s attack miss.')
            return 0

    def info(self):
        system('cls')
        print(self.name,
              f'\nHealth {self.hp}/{self.max_hp}',
              f'\nAttack {self.atk}')
        input('\nPress any key to continue...')

    def targetInfo(self):
        return f'{self.name}\t\t({self.hp}/{self.max_hp})'


# FOR TESTING PURPOSES
# enemy1 = Enemy('Slime', 50, 15)
# enemy1.receiveDmg(999)
