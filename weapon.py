class Weapon:
    def __init__(self, data: list):
        self.__name = data[0]
        self.__attack = data[1]
        self.__accuracy = data[2]
        self.__pellet = data[3]

    def get(self, stat):
        return self.__dict__['_Weapon__'+stat]

    def fetchStat(self):
        return {
            'name': self.__name,
            'attack': self.__attack,
            'accuracy': self.__accuracy,
            'pellet': self.__pellet
        }

    def info(self):
        print("Weapon Name : " + self.__name)
        print('Attack : ' + self.__attack)
        print('Accuracy : ' + self.__accuracy)
        print('Pellet Count : ' + self.__pellet)


# FOR TESTING PURPOSES
wpn1 = Weapon(['AK-47', 40, 0.55, 1])
print(wpn1.get('name'))
# wpn1.info()
