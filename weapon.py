class weapon:
    def __init__(self, name, acc, dmg):
        self.name = name
        self.acc = acc
        self.dmg = dmg

    def getName(self):
        print("Weapon Name : " + self.name)

    def m4(self):
        print("Your weapon : " + self.name)


# object construct taro base, ini biarin buat testing
# klo gk sekalian aja bikin database weapons sama enemies biar sekalian di construct semua di situ
wpn1 = weapon("Ak-47", 0.6, 40)
wpn2 = weapon("M4A1", 0.8, 25)
wpn1.ak()
