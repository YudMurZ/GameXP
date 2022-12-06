import time
import random
from os import system
from typing import List
from enemy import Enemy
from weapon import *


class Player:
    def __init__(self, name):
        self.__name = name
        self.__level = 1
        self.__exp = 0
        self.__max_health = self.__health = 100
        self.__weapon: Weapon
        self.__attack = None
        self.__accuracy = None
        self.__agility = 50

    def get(self, stat):
        return self.__dict__['_Player__'+stat]

    def equipWeapon(self, weapon: Weapon):
        self.__weapon = weapon
        weapon = weapon.fetchStat()
        self.__attack = weapon['attack']
        self.__accuracy = weapon['accuracy']
        print(f'\n{weapon["name"]} is equipped.')

    def switchWeapon(self, weapon: Weapon):
        old = self.__weapon.fetchStat()
        new = weapon.fetchStat()
        self.__attack -= old['attack'] + new['attack']
        self.__accuracy -= old['accuracy'] + new['accuracy']
        print(f'\n{weapon["name"]} is equipped.')

    def action(self, opponents):
        system('cls')
        print(
            f'{self.__name} ({self.__health}/{self.__max_health})',
            '\n 1. Attack',
            '\n 2. Info',
            '\n 3. Run'
        )
        opt = input('Select Action : ')

        if opt == '1':
            # Attack opponent
            print('\nATTACK')
            for i, enemy in enumerate(opponents):
                print(f' {i+1}. {enemy.name} ({enemy.hp}/100)')
            print(f' 0. Back')
            target = int(input('Select target : '))
            if target == 0 or target > len(opponents):
                self.action(opponents)
            else:
                return [self.attack(opponents[target-1]), target-1]

        elif opt == '2':
            # Info
            print(f'\nINFO\n 1. {self.__name}')
            for i, enemy in enumerate(opponents):
                print(f' {i+2}. {enemy.name}')
            print(f' 0. Back')
            target = int(input('Select target : '))
            if target == 1:
                self.info()
            elif target in range(2, len(opponents)+2):
                opponents[target-2].info()
            self.action(opponents)

        elif opt == '3':
            # Run away
            system('cls')
            print('Running away...')
            time.sleep(1)
            print('You fled.')
            time.sleep(2)
            return 'flee'

        else:
            return self.action(opponents)

    def attack(self, target: Enemy):
        system('cls')
        print('Attacking....')
        time.sleep(2)
        if random.uniform(0, 1) <= self.weapon.acc:
            return target.receiveDmg(self.weapon.atk * self.weapon.pellet)
        else:
            print('Attack missed.')
            return

    def receiveDmg(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            print('You are Dead.')
            del self
        else:
            print('You received ' + str(dmg) + ' damage.')
            time.sleep(2)
        return

    def info(self):
        system('cls')
        print(self.__name,
              f'\nHealth   {self.__health}/{self.__max_health}',
              f'\n\n{self.__weapon.get("name")}',
              f'\nAttack   {self.__weapon.get("name")}',
              f'\nAccuracy {int(self.__weapon.get("acc")*100)}%',
              f'\nPellet   {self.__weapon.get("pellet")}',
              f'\nAgility  {self.__agility}')
        input('\nPress Enter to continue...')


# FOR TESTING PURPOSE
# player = Player('udin')
# print(player.get('agility'))
