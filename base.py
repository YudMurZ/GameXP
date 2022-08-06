from ast import For
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
    mainmenu()


def mainmenu():
    print("Welcome to game-ish")
    time.sleep(2)
    print(" 1. Play")
    print(" 2. Exit")

    opt = input("Enter the number : ")
    if opt == 1:
        game()
    else:
        sys.exit()


def game():

    player = human(input("Input your username : "))
    time.sleep(2)
    print("Hello " + player.name + ". Welcome to the game")
    time.sleep(2)
    print("Weapon available :")
    print("1. Ak-47")
    print("2. M4A1")
    print("3. Mp5")

    weapon = int(input("Enter your weapon : "))
    if weapon == 1:
        wpn1()

    print("Enemy Difficulty :")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")

    # difficulty = int(input("Select enemy difficulty : "))


def wpn1():
    print(weapons[0])
    damage = 400
    hit = random.uniform(0, 1)
    print("Firing...")
    if hit >= 0.1:

        time.sleep(2)
        print("Target Hit!")
        enemies[1][1] = enemies[1][1] - damage
        if enemies[1][1] <= 0:
            print("Target Eliminated!")
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
            print("Target Remaining health :" + str(enemies[1][1]))

    else:
        print("Missed!")


main()
# if difficulty ==1:
# print("Enemy turn!")
# print("Enemy Attacking!")
