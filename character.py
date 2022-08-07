class Player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.weapon = 'Unequipped'
        self.eva = 50

    def stats(self):
        print('Name : '+self.name)
        print('HP : ' + str(self.health))
        print('Weapon : ' + self.weapon.name)
        print('Evasion : ' + str(self.eva))

    def equipWeapon(self, weapon):
        self.weapon = weapon
        print(self.weapon.name + ' is equipped.')

    def action(self, opponents):
        print('PLAYER TURN\n\n1. Attack\n2. Run')
        opt = input('Select Action : ')
        if opt == '1':
            print('OPPONENTS')
            i = 1
            while i < len(opponents):
                if i == len(opponents):
                    print(str(i) + '. Back')
                else:
                    print(
                        str(i) + ". " + opponents[i-1].targetInfo())
                    i += 1
            target = input('Select target : ')
            if target == i:
                self.action()
            else:
                self.attack(opponents[target-1])
        elif opt == '2':
            print('You are running away...')
            time.sleep(2)
            print('You fled.')
            time.sleep(2)
        else:
            self.action()

    def attack(self, target):
        print('Attacking....')
        time.sleep(2)
        if random.uniform(0, 1) <= self.acc:
            target.health -= self.weapon.dmg
            print(target.name + ' received ' +
                  str(self.weapon.dmg) + ' damage.')
            time.sleep(1)
            if target.health <= 0:
                del target
                print(target.name + ' is dead!')
            return
        else:
            print('Attack missed.')
            return
