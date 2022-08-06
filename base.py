import random
import sys
import time
from weapon import weapon

health = 100
enemyEasy = 50
enemyNormal = 100
enemyHard = 200


def main():
    mainmenu()



def mainmenu():
    name = input("Input your username : ")
    time.sleep(2)
    print("Welcome to game-ish " + name)
    time.sleep(2)
    print("Press 1 to start the game and press 2 to stop the game")
    opt = int(input("Select 1 or 2 : "))
    if opt ==1:
        game()


def game():

    print("Weapon available :")
    print("1. Ak-47")
    print("2. M4A1")
    print("3. Mp5")

    weapon = int(input("Enter your weapon : "))
    if weapon ==1:
        wpn1(enemyNormal)


    print("Enemy Difficulty :")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")

    #difficulty = int(input("Select enemy difficulty : "))

def wpn1(enemyNormal):
    print("Ak-47 selected")
    damage = 400
    hit = random.uniform(0,1)
    print("Firing...")
    if hit >= 1:
        
        time.sleep(2)
        print("Target Hit!")
        enemyNormal = enemyNormal - damage
        if enemyNormal <= 0:
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
            if pick ==1:
                game()
            

        else:
            print("Target Remaining health :" + str(enemyNormal))
    
    else: 
        print("Missed!")
main()
#if difficulty ==1:
    #print("Enemy turn!")
    #print("Enemy Attacking!")

