import time
import random
from os import system


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = 'Unequipped'
        self.atk = 0
        self.acc = 0
        self.eva = 50

    def stats(self):
        print('Name : ' + self.name)
        print('Weapon : ' + self.weapon.name)
        print('HP : ' + str(self.health))
        print('Attack : ' + str(self.atk))
        print('Accuracy : ' + str(self.acc*100) + '%')
        print('Evasion : ' + str(self.eva))

    def equipWeapon(self, weapon):
        self.weapon = weapon
        self.atk = weapon.atk
        self.acc = weapon.acc
        print(self.weapon.name + ' is equipped.')

    def action(self, opponents):
        system('cls')
        print(f'{self.name} ({self.health}/100)\n 1. Attack\n 2. Run')
        opt = input('Select Action : ')
        if opt == '1':
            system('cls')
            print('OPPONENTS')
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
        else:
            self.action()

    def attack(self, target):
        system('cls')
        print('Attacking....')
        time.sleep(2)
        if random.uniform(0, 1) <= self.acc:
            return target.receiveDmg(self.atk)
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
