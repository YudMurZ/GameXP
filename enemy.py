import random


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.max_hp = health
        self.hp = health
        self.atk = attack

    def receiveDmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            print(self.name + ' is dead.')
            return 'enemy die'
        else:
            print(self.name + ' received ' + str(dmg) + ' damage.')

    def attack(self, target):
        if random.uniform(0, 1) >= target.eva:
            print(self.name + ' hit you.')
            target.receiveDmg(self.atk)
        else:
            print(self.name + '\'s attack miss.')
            return 0

    def targetInfo(self):
        # hp = str(self.hp)
        # max_hp = str(self.max_hp)
        return f'{self.name}\t\t({self.hp}/{self.max_hp})'


# FOR TESTING PURPOSES
# easy = Enemy('Slime', 50)
# normal = Enemy('Goblin', 100)
# hard = Enemy('Golem', 200)
# easy.attack()
# normal.attack()
# hard.attack()
