class human:
    def __init__(self, health):
       self.health = health

    def chara(self):
        print("Your health : " + str(self.health))

obj = human(100)
obj.chara()
