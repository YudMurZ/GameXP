class enemy:
    def __init__(self, health):
       self.health = health

    def target(self):
        print("Enemy health : " + str(self.health))

easy = enemy(50)
normal = enemy(100)
hard = enemy(200)
easy.target()
normal.target()
hard.target()
