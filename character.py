import time
import random
from os import system
from unicodedata import name


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None
        self.eva = 50

    def info(self):
        print(f'Name : {self.name}')
        print(f'Weapon : {self.weapon.name}')
        print(f'HP : {self.health}')
        print(f'Attack : {self.weapon.atk}')
        print(f'Accuracy : {self.weapon.acc*100}%')
        print(f'Evasion : {self.eva}')

    def equipWeapon(self, weapon):
        self.weapon = weapon
        print(f'{self.weapon.name} is equipped.')
        time.sleep(2)

    def action(self, opponents):
        system('cls')
        print(f'{self.name} ({self.health}/100)\n 1. Attack\n 2. Run')
        opt = input('Select Action : ')
        if opt == '1':
            print('\nOPPONENTS')
            i = 1
            while i <= len(opponents):
                print(str(i) + ". " + opponents[i-1].targetInfo())
                i += 1
            print(str(i) + '. Back')
            target = int(input('Select target : '))
            if target > len(opponents):
                self.action(opponents)
            else:
                return [self.attack(opponents[target-1]), target-1]
        elif opt == '2':
            system('cls')
            print('You are running away...')
            time.sleep(1)
            print('You fled.')
            time.sleep(2)
            return 'flee'

        elif opt == '3':
            print(
                f'Weapon Damage : {self.weapon.atk} \nWeapon Hit Chance : {self.weapon.acc*100}')

        else:
            self.action()

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
