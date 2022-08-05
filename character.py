class human:
    def __init__(self, health):
       self.health = health
       self.weapon = None

    def chara(self):
        print("Your health : " + str(self.health))

obj = human(100)
obj.chara()
