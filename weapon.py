class Weapon:
    def __init__(self, data: list):
        self.name = data[0]
        self.atk = data[1]
        self.acc = data[2]

    def info(self):
        print("Weapon Name : " + self.name)
        print('Attack : ' + self.atk)
        print('Accuracy : ' + self.acc)

# FOR TESTING PURPOSES
# wpn1 = Weapon('AK-47', 40, 0.55)
# wpn1.info()
