class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def getHealth(self):
        print(self.name + "'s HP: " + str(self.health))

# FOR TESTING PURPOSES
# easy = enemy('Slime', 50)
# normal = enemy('Goblin', 100)
# hard = enemy('Golem', 200)
# easy.getHealth()
# normal.getHealth()
# hard.getHealth()
