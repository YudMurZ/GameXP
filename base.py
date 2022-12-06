import sys
import time
from os import system
from database import *
from character import *

player = None
opponents = []


def main():
    # mainMenu()
    battleMode(selectionMode())


def mainMenu():
    print('Welcome to game-ish')
    time.sleep(2)
    print(' 1. Play\n 2. Exit')
    opt = input('Enter number : ')
    if opt == '1':
        return
    else:
        sys.exit()


def selectionMode():
    system('cls')
    global player
    player = Player(input('Input player name : '))
    print('\nHello, ' + player.name + '. Welcome to the game!')
    time.sleep(2)

    system('cls')
    print('WEAPONS')
    for i, weapon in enumerate(weapons):
        print(
            f'{i+1}. {weapon[0]} (ATK {weapon[1]} | ACC {int(weapon[2]*100)}%) | Pellet {weapon[3]}')
    choice = int(input('Enter your weapon : '))
    player.equipWeapon(Weapon(weapons[choice-1]))
    time.sleep(2)

    system('cls')
    print('DIFFICULTY\n 1. Easy\n 2. Normal\n 3. Hard')
    return int(input('Select your difficulty : '))


def battleMode(diff):
    if diff == 1:
        difficulty = 'Easy'
    elif diff == 2:
        difficulty = 'Normal'
    elif diff == 3:
        difficulty = 'Hard'
    system('cls')
    print(f'Battle Mode ({difficulty})\n')
    time.sleep(1)

    global opponents
    global player
    for i in range(1):
        opponents.append(Enemy(enemies[diff-1]))
        print(opponents[i].name + ' is approaching.')
    time.sleep(2)
    while (len(opponents) > 0):
        system('cls')
        print('PLAYER TURN')
        time.sleep(1)
        action = player.action(opponents)
        if action == 'flee':
            restart()
        elif isinstance(action, list):
            if action[0] == 'enemy die':
                del opponents[action[1]]
        if len(opponents) == 0:
            print("You win!")
            time.sleep(2)
            restart()
        else:
            system('cls')
            print('OPPONENTS TURN')
            time.sleep(1)
            for i in opponents:
                i.attack(player)


def restart():
    system('cls')
    print("Play again?\n 1. Yes\n 2. No")
    pick = int(input("Select your choice : "))
    if pick == 1:
        selectionMode()
    else:
        sys.exit()


main()
