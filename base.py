# import random
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
    print('Hello, ' + player.name + '. Welcome to the game')
    time.sleep(2)

    system('cls')
    print('WEAPON')
    # for i in weapons:
    #     print(i[0])
    for i, weapon in enumerate(weapons):
        print(f'{i+1}. {weapon.name} (ATK {weapon.atk} | ACC {int(weapon.acc*100)}%)')
    weapon = int(input('Enter your weapon : '))
    # player.equipWeapon(Weapon(weapon-1))
    player.equipWeapon(weapons[weapon-1])
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
    print(f'Battle Mode ({difficulty})')

    global opponents
    global player
    for i in range(0, 1):
        opponents.append(enemies[diff-1])
        print(opponents[i].name + ' approaching you.')
    time.sleep(2)
    while (len(opponents) > 0):
        print('PLAYER TURN')
        time.sleep(2)
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
            print('OPPONENTS TURN')
            time.sleep(2)
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


# def easy():
#     print(weapons[0].name)
#     time.sleep(2)

#     battle_enemy_1 = enemies[1]
#     damage = weapons[0].dmg
#     hit = random.uniform(0, 1)
#     print("Firing...")
#     if hit >= weapons[0].acc:
#         time.sleep(2)
#         print("Target Hit!")
#         enemyHP = enemies[1].health - damage
#         if enemyHP <= 0:
#             del battle_enemy_1
#             time.sleep(2)
#             print("Mission accomplished! \n")
#             time.sleep(2)
#             print("Play again?")
#             print("1. Yes")
#             print("2. No")
#             pick = int(input("Select your choice : "))
#             if pick == 2:
#                 sys.exit()
#             if pick == 1:
#                 selectionMode()

#         else:
#             print("Target Remaining health :" + str(enemyHP))
#             time.sleep(2)
#             print("Enemy Turn!")
#             enemyATK1()

#     else:
#         dmg = 0
#         enemyHP = enemies[1].health - dmg
#         time.sleep(2)
#         print("Missed!")
#         print("Target Remaining health :" + str(enemyHP))
#         time.sleep(2)
#         enemyATK1()


# def enemyATK1():
#     time.sleep(2)
#     battle_enemies_atk_1 = enemies[1]
#     player_cond = Player
#     attack = enemies[1].attack
#     hit = enemies[1].acc
#     chance = random.uniform(0, 1)
#     if hit <= chance:
#         print("You are hit!")
#         playerHP = Player.health - attack

#         if playerHP <= 0:
#             print("You are dead!")

#         else:
#             print("Your health = " + str(playerHP))

#     else:
#         print("Enemy Missed!")


main()
# if difficulty ==1:
# print("Enemy turn!")
# print("Enemy Attacking!")
