import time
import random
from os import system
from weapon import *


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None
        self.eva = 50

    def info(self):
        system('cls')
        print(self.name,
              f'\nWeapon   {self.weapon.name}',
              f'\nHealth   {self.health}/100',
              f'\nAttack   {self.weapon.atk}',
              f'\nAccuracy {int(self.weapon.acc*100)}%',
              f'\nEvasion  {self.eva}')
        input('\nPress Enter to continue...')

    def equipWeapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f'\n{self.weapon.name} is equipped.')

    def action(self, opponents):
        system('cls')
        print(f'{self.name} ({self.health}/100)\n 1. Attack\n 2. Info\n 3. Run')
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
            print(f'\nINFO\n 1. {self.name}')
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

    def attack(self, target):
        system('cls')
        print('Attacking....')
        time.sleep(2)
        if random.uniform(0, 1) <= self.weapon.acc:
            return target.receiveDmg(self.weapon.atk)
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
