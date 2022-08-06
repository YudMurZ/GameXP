from ast import For
from os import system
import random
import sys
import time
from character import human
from database import *

# FOR TESTING PURPOSES
# health = 100
# enemyEasy = 50
# enemyNormal = 100
# enemyHard = 200


def main():
    # mainMenu()
    game()


def mainMenu():
    print("Welcome to game-ish")
    time.sleep(2)
    print(" 1. Play\n 2. Exit")
    opt = input("Enter the number : ")
    if opt == "1":
        selectionMode()
    else:
        sys.exit()


def selectionMode():
    player = human(input("Input your username : "))
    print("Hello, " + player.name + ". Welcome to the game")
    time.sleep(2)

    weapon_input = False
    while weapon_input == False:
        print("Weapon available :")
        for i in range(1, len(weapons)+1):
            print(str(i) + ". " + weapons[i-1].name)

        weapon = input("Enter your weapon : ")
        if weapon == "1":
            human.equipWeapon(weapons[0])
            weapon_input = True
        elif weapon == "2":
            human.equipWeapon(weapons[1])
            weapon_input = True
        elif weapon == "3":
            human.equipWeapon(weapons[2])
            weapon_input = True
        else:
            print("Invalid input")
            weapon_input = False
            system('cls')

    difficulty_input = False
    while difficulty_input == False:
        print("Select your difficulty :\n1. Easy\n2. Normal\n3. Hard")
        difficulty = input("Select your difficulty : ")
        if difficulty == "1":
            wpn1()
            difficulty_input = True
        # elif difficulty == "2":
        #     normal()
        #     difficulty_input = True
        # elif difficulty == "3":
        #     hard()
        #     difficulty_input = True
        else:
            print("Invalid input")
            difficulty_input = False
            system('cls')


def wpn1():
    print(weapons[0].name)
    battle_enemy_1 = enemies[1]
    damage = weapons[0].dmg
    hit = random.uniform(0, 1)
    print("Firing...")
    if hit >= weapons[0].acc:
        time.sleep(2)
        print("Target Hit!")
        enemyHP = enemies[1].health - damage
        if enemyHP <= 0:
            del battle_enemy_1
            time.sleep(2)
            print("Mission accomplished! \n")
            time.sleep(2)
            print("Play again?")
            print("1. Yes")
            print("2. No")
            pick = int(input("Select your choice : "))
            if pick == 2:
                sys.exit()
            if pick == 1:
                game()

        else:
            print("Target Remaining health :" + str(enemies[1].health))

    else:
        time.sleep(2)
        print("Missed!")


main()
# if difficulty ==1:
# print("Enemy turn!")
# print("Enemy Attacking!")
