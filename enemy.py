class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.max_hp = health
        self.hp = health
        self.atk = attack

    def __del__(self):
        print(self.name + ' is dead.')

        return

    def receiveDmg(self, dmg, target_index):
        self.hp -= dmg
        if self.hp <= 0:
            opponents.pop(target_index)
            del self
        else:
            print(self.name + ' received ' + str(dmg) + ' damage.')

    def attack(self, target):
        if random.uniform(0, 1) >= target.eva:
            print(self.name + ' hit you.')
            return self.atk
        else:
            print(self.name + '\'s attack miss.')
            return 0

    def targetInfo(self):
        print(self.name + ' (' + str(self.hp) + '/' + str(self.atk) + ')')


# FOR TESTING PURPOSES
# easy = Enemy('Slime', 50)
# normal = Enemy('Goblin', 100)
# hard = Enemy('Golem', 200)
# easy.attack()
# normal.attack()
# hard.attack()
