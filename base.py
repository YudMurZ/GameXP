from os import system
from Character import *
from Database import *
import random
import sys
import time
from database import *
from character import *
from os import system


def main():
    # mainMenu()
    selectionMode()


def mainMenu():
    print('Welcome to game-ish')
    time.sleep(2)
    print(' 1. Play\n 2. Exit')
    opt = input('Enter number : ')
    if opt == '1':
        selectionMode()
    else:
        sys.exit()


def selectionMode():
    system('cls')
    player = Human(input('Input player name : '))
    print('Hello, ' + player.name + '. Welcome to the game')
    time.sleep(2)

    system('cls')
    print('WEAPON')
    for i in range(1, len(weapons)+1):
        print(str(i) + ". " + weapons[i-1].name)
    weapon = int(input("Enter your weapon : "))
    player.equipWeapon(weapons[weapon-1])

    # diff_input = False
    # while diff_input == False:
    system('cls')
    print('DIFFICULTY\n1. Easy\n2. Normal\n3. Hard')
    battleMode(player, int(input('Select your difficulty : ')))


def battleMode(player, diff):
    if diff == 1:
        difficulty = 'Easy'
    elif diff == 2:
        difficulty = 'Normal'
    elif diff == 3:
        difficulty = 'Hard'
    system('cls')
    enemy = enemies[diff-1]
    print("Battle Mode (" + difficulty + ")")
    time.sleep(2)

    # action = False
    # while action == False:
    system('cls')
    print('PLAYER TURN\n1. Attack\n2. Run')
    opt = input('Select Action : ')
    if opt == '1':
        # action = True
        player.attack(enemy)
    elif opt == '2':
        # action = True
        print('You are running away...')
        time.sleep(2)
        print('You fled.')
        time.sleep(2)
        # else:
        #     print('Invalid input')
        #     action = False

    system('cls')
    print('Play again?\n1. Yes\n2. No')
    pick = int(input('Select your choice : '))
    if pick == 2:
        sys.exit()
    if pick == 1:
        selectionMode()


def easy():
    print(weapons[0].name)
    time.sleep(2)

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
                selectionMode()

        else:
            print("Target Remaining health :" + str(enemyHP))
            time.sleep(2)
            print("Enemy Turn!")
            enemyATK1()

    else:
        dmg = 0
        enemyHP = enemies[1].health - dmg
        time.sleep(2)
        print("Missed!")
        print("Target Remaining health :" + str(enemyHP))
        time.sleep(2)
        enemyATK1()


def enemyATK1():
    time.sleep(2)
    battle_enemies_atk_1 = enemies[1]
    player_cond = Human
    attack = enemies[1].attack
    hit = enemies[1].acc
    chance = random.uniform(0, 1)
    if hit <= chance:
        print("You are hit!")
        playerHP = Human.health - attack

        if playerHP <= 0:
            print("You are dead!")

        else:
            print("Your health = " + str(playerHP))

    else:
        print("Enemy Missed!")


main()
# if difficulty ==1:
#print("Enemy turn!")
#print("Enemy Attacking!")
