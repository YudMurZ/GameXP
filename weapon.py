class Weapon:
    def __init__(self, name, acc, dmg):
        self.name = name
        self.acc = acc
        self.dmg = dmg

    def getName(self):
        print("Weapon Name : " + self.name)

# FOR TESTING PURPOSES
# wpn1 = weapon("Ak-47", 0.6, 40)
# wpn2 = weapon("M4A1", 0.8, 25)
# wpn1.getName()
