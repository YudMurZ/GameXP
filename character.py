class human:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None

    def chara(self):
        print(self.name + "'s HP : " + str(self.health))

    def equipWeapon(self, weapon):
        self.weapon = weapon
        print(self.weapon + " is equipped.")

    def getWeapon(self):
        print("Your Weapon : " + self.weapon)
