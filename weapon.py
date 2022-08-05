class weapon:
    def __init__(self, name, acc, dmg):
       self.name = name
       self.acc = acc
       self.dmg = dmg

    def ak(self):
        print("Your weapon : " + self.name)

    def m4(self):
        print("Your weapon : " + self.name)

wpn1 = weapon("Ak-47", "60%", 40)
wpn2 = weapon("M4A1", "80%", 25)
wpn1.ak()
