class enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def getHealth(self):
        print(self.name + "'s HP: " + str(self.health))


# cek comment di weapon.py
easy = enemy('Slime', 50)
normal = enemy('Goblin', 100)
hard = enemy('Golem', 200)
easy.getHealth()
normal.getHealth()
hard.getHealth()
