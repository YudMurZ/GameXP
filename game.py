import time
from character import Player
from enemy import Enemy
from database import *


class Game:
    def __init__(self, player: Player, foe: Enemy):
        self.__player = player
        self.__foe = foe

    def generatePlayer(self):

        # PLAYER NAME INPUT
        self.__player = Player(input('\nInput player name : '))
        print(f'\nHello, {self.__player.get("name")}. Welcome to the game!')
        time.sleep(2)

        # STARTER WEAPON INPUT
        print('WEAPONS')
        for i, weapon in enumerate(weapons):
            print(
                f'{i+1}. {weapon[0]} (ATK {weapon[1]} | ACC {int(weapon[2]*100)}%) | Pellet {weapon[3]}')
        choice = int(input('Enter your starter weapon : '))
        self.__player.equipWeapon(Weapon(weapons[choice-1]))
        time.sleep(2)

    def difficultySelection():
        print('\nDIFFICULTY\n 1. Easy\n 2. Normal\n 3. Hard\n')
        return int(input('Select your difficulty : '))

    def battle(self, difficulty):

        print(f'Battle Mode\n')
        time.sleep(1)

        # GENERATE MULTIPLE ENEMIES
        # for i in range(3):
        #     self.__foe.append(Enemy(enemies[difficulty-1]))
        #     print(self.__foe[i].get('name') + ' is approaching.')
        # time.sleep(2)

        # GENERATE SINGLE ENEMY
        self.__foe = Enemy(enemies[difficulty-1])
        print(self.__foe.get("name") + ' is approaching.')

        if self.__player.health < 0:
            print('You lose')

        elif len(self.__foe) < 0:
            print('You win!')

        else:
            ally_speed = self.__player.get('agility')
            foe_speed = max(enemy.get('agility') for enemy in self.__foe)

            if ally_speed >= foe_speed:
                print('PLAYER TURN')
                self.__player.action(self.__foe)
                print('ENEMY TURN')
                for enemy in self.__foe:
                    enemy.attack(self.__player)
            else:
                print('ENEMY TURN')
                for enemy in self.__foe:
                    enemy.attack(self.__player)
                print('PLAYER TURN')
                self.__player.action(self.__foe)

        self.battle(difficulty)
