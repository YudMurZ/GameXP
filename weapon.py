class Weapon:
    def __init__(self, name, attack, accuracy):
        if isinstance(name, list):
            self.name = name[0]
            self.atk = name[1]
            self.acc = name[2]
        else:
            self.name = name
            self.atk = attack
            self.acc = accuracy

    def info(self):
        print("Weapon Name : " + self.name)
        print('Attack : ' + self.atk)
        print('Accuracy : ' + self.acc)

# FOR TESTING PURPOSES
# wpn1 = Weapon('AK-47', 40, 0.55)
# wpn1.info()
