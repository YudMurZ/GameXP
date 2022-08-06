from os import system
from Character import *
from Database import *
import random
import sys
import time

# FOR TESTING PURPOSES
# health = 100
# enemyEasy = 50
# enemyNormal = 100
# enemyHard = 200


def main():
    # mainMenu()
    selectionMode()


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
    player = Human(input("Input your username : "))
    print("Hello, " + player.name + ". Welcome to the game")
    time.sleep(2)

    print("Weapon available :")
    for i in range(1, len(weapons)+1):
        print(str(i) + ". " + weapons[i-1].name)
    weapon = int(input("Enter your weapon : "))
    player.equipWeapon(weapons[weapon-1])

    difficulty_input = False
    while difficulty_input == False:
        print("Select your difficulty :\n1. Easy\n2. Normal\n3. Hard")
        difficulty = input("Select your difficulty : ")
        if difficulty == "1":
            easy()
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


def easy():
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
        
def enemyATK1():
    time.sleep(2)
    battle_enemies_atk_1 = enemies[1]
    player_cond = human
    attack = enemies[1].attack
    hit = enemies[1].acc
    chance = random.uniform(0,1)
    if hit <= chance:
        print("You are hit!")
        playerHP = human.health - attack
       
        if playerHP <= 0:
            print("You are dead!")

        else:
             print("Your health = " + playerHP)


    else:
        print("Enemy Missed!")


main()
# if difficulty ==1:
# print("Enemy turn!")
# print("Enemy Attacking!")
