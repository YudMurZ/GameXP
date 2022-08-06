class Weapon:
    def __init__(self, name, attack, accuracy):
        self.name = name
        self.atk = attack
        self.acc = accuracy

    def info(self):
        print("Weapon Name : " + self.name)
        print('Attack : ' + self.atk)
        print('Accuracy : ' + self.acc)

# FOR TESTING PURPOSES
# wpn1 = weapon("Ak-47", 0.6, 40)
# wpn2 = weapon("M4A1", 0.8, 25)
# wpn1.getName()
