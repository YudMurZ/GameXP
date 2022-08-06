import random


class Human:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = 'Unequipped'
        self.eva = 50

    def stats(self):
        print('Name : '+self.name)
        print('HP : ' + str(self.health))
        print('Weapon : ' + self.weapon.name)
        print('Evasion : ' + str(self.eva))

    def equipWeapon(self, weapon):
        self.weapon = weapon
        print(self.weapon.name + ' is equipped.')

    def attack(self, target):
        pass
