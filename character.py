class human:
    def __init__(self, health):
       self.health = health
       self.weapon = None

    def chara(self):
        print("Your health : " + str(self.health))

    def equip(self, weapon):
        self.weapon = weapon
        print("You have equipped " + self.weapon)

obj = human(100)
obj.chara()
