from audioop import add
import random
import time
from os import system
from character import Player


class Enemy:
    def __init__(self, data: list):
        self.__name = data[0]
        self.__max_health = self.__health = data[1]
        self.__atk = data[2]
        self.__agility = data[3]

    def get(self, stat):
        return self.__dict__['_Enemy__'+stat]

    def receiveDmg(self, damage):
        self.__health -= damage
        print(f'{self.__name} received {damage} damage.')
        time.sleep(2)
        if self.__health <= 0:
            print(self.__name + ' is dead.')
            return 'enemy die'

    def attack(self, target: Player):
        system('cls')
        if random.uniform(0, 1) >= target.__agility/100:
            print(self.__name + ' hit you.')
            target.receiveDmg(self.atk)
        else:
            print(self.__name + '\'s attack miss.')
            return 0

    def info(self):
        system('cls')
        print(self.__name,
              f'\nHealth {self.__health}/{self.__max_health}',
              f'\nAttack {self.__atk}')
        input('\nPress any key to continue...')

    def targetInfo(self):
        return f'{self.__name}\t\t({self.__health}/{self.__max_health})'


# FOR TESTING PURPOSES
enemy1 = Enemy(['Slime', 50, 15, 10])
# print(enemy1.getStat('agility'))
# enemy1.receiveDmg(999)
