import math
import random
import collections
from engine import cls
from player_functions import *
from dictionaries import *
red = "\033[1;31;40m"
blue = "\033[1;34;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
default = "\033[1;37;40m"

def print_stats():
        print("Name:", player["name"])
        print("Hit Points:", green + player["Hit Points"] + default)
        print("EXP:", player["EXP"])
        print("EXP to next level:", yellow + player["EXP to next level"] + default)
        print("Current Level:", green + player["level"] + default)
        print("Attack points:", red + player["Attack Points"] + default)
        print("Defense points:", blue + player["Defense Points"] + default)

def fighting():
   # player["Name"] = input("What is your name: ").capitalize()
    cls()
    # you can get rid of the instructions when adding to main game if you want ^

    again = True

    # Set up the play again loop
    while again:
        robotgen = list(robots.keys())
        
        robot = random.choice(robotgen).lower()

        winner = None
        player["Hit Points"] = 100
        enemyhealth = 100
        print("Oh no! A robot", red +(random.choice(robotgen)).upper() + default, "appeared!")
        print("-----------------------")

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            turn_player = True
            turn_enemy = False
            print("You will go first.")
            print("-----------------------")
        else:
            turn_player = False
            turn_enemy = True
            print("Your enemy will go first.")
            print("-----------------------")
        print("Your health: ", green + str(player["Hit Points"]) + default)
        print("Enemy health: ", red + str(enemyhealth) + default)

        #main game loop
        while (player["Hit Points"] != 0 or enemyhealth != 0):
            heal = False
            miss = False
            moves = {"Punch": random.randint(15,25),
                 "Kick": random.randint(12,35),
                 "Karate Chop": random.randint(10,30),
                 "Heal": random.randint(20,30)}
            if turn_player:
                print("You can: ")
                print("1. Punch (15-25 damage)")
                print("2. Kick (12-35 damage)")
                print("3. Karate Chop (10-30)")
                print("4. Heal (Heal by 20-30)")
                print("5. View stats")
                print("-----------------------")
                
                playerchoice = input("Select a move: ").lower()
                cls()
                print("-----------------------")
                chance_of_miss = random.randint(1,5) # 1 in 5 chance player misses

                if chance_of_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    playerchoice = 0 # player misses and deals no damage
                    print("You missed!")
                else:
                    if playerchoice in ("1", "punch"):
                        playerchoice = moves["Punch"]
                        print("You swing left and right and land a good punch. Damage:", playerchoice)
                    elif playerchoice in ("2", "kick"):
                        playerchoice = moves["Kick"]
                        print("You kicked your enemy to the ground. Damage:", playerchoice)
                    elif playerchoice in ("3", "karate chop"):
                        playerchoice = moves["Karate Chop"]
                        print("You karate chopped your enemy. Ouch! Damage: ", playerchoice)
                    elif playerchoice in ("4", "heal"):
                        if player["Inventory"] < 1:
                            print("You are out of potions!")
                            print("Your health: ", player["Hit Points"], "Enemy health: ", enemyhealth)
                            continue
                        else:
                            heal = True # heal activated
                            playerchoice = moves["Heal"]
                            print("You heal yourself! You've gained", playerchoice, "health")
                    elif playerchoice in ("5", "view stats"):
                        print_stats()
                        print("-----------------------")
                        #playerchoice = input("Select a move: ").lower()
                        continue
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    enemychoice = 0 # the computer misses and deals no damage
                    print("The robot missed!")
                else:
                    if enemyhealth > 30:
                        if enemyhealth > 75:
                            enemychoice = moves["Punch"]
                            print("Your enemy punches you straight in the face. Damage:", enemychoice)
                        elif player["Hit Points"] > 35 and player["Hit Points"] <= 75:
                            move_choice = ["Punch", "Kick", "Karate Chop"]
                            move_choice = random.choice(move_choice)
                            enemychoice = moves[move_choice]
                            print("Your enemy used", move_choice, "Damage:", enemychoice)
                        elif player["Hit Points"] <= 35:
                            enemychoice = moves["Kick"]
                            print("Your enemy kicks you to the floor! Damage:", enemychoice)                     
                    else: # if the computer has less than 30 health, there is a 50% chance they will heal
                        choice5050 = random.randint(1,2) 
                        if choice5050 == 1:
                            heal = True
                            enemychoice = moves["Heal"]
                            print("Your enemy chose to heal. Their health increased by ", enemychoice)
                        else:
                            if player["Hit Points"] > 75:
                                enemychoice = moves["Punch"]
                                print("Your enemy lands a hard punch right on your nose! Damage:", enemychoice)
                            elif player["Hit Points"] > 35 and player["Hit Points"] <= 75:
                                move_choice = ["Punch", "Kick", "Karate Chop"]
                                move_choice = random.choice(move_choice)
                                enemychoice = moves[move_choice]
                                print("Your enemy used ", move_choice, ". Damage:", enemychoice)
                            elif player["Hit Points"] <= 35:
                                enemychoice = moves["Kick"] 
                                print("Your enemy kicked you. Ouch! Damage:", enemychoice)

            if heal:
                if turn_player:
                    player["Hit Points"] += playerchoice
                    player["Inventory"] -=1
                    if player["Hit Points"] > 100:
                        player["Hit Points"] = 100 # cap max health at 100. No over healing!
                        
                else:
                    enemyhealth += enemychoice
                    if enemyhealth > 100:
                        enemyhealth = 100
            else:
                if turn_player:
                    enemyhealth -= playerchoice
                    xp = (playerchoice*random.uniform(0.1,1))
                    xp = round(xp, 0)
                    player["EXP"] = round(player["EXP"] + xp, 0)
                    if enemyhealth < 0:
                        enemyhealth = 0 # cap minimum health at 0
                        winner = "Player"
                        break
                else:
                    player["Hit Points"] -= enemychoice
                    if player["Hit Points"] < 0:
                        player["Hit Points"] = 0
                        winner = "Enemy"
                        break
            if player["EXP"] >= player["EXP to next level"]:
                print("Level Up!!")
                level_up()
                if player["Hit Points"] > 100:
                    player["Hit Points"] = 100
                #print("-----------------------")   
                #print_stats()
                #print("-----------------------")
            


            # switch turns
            turn_player = not turn_player
            turn_enemy = not turn_enemy
            if not turn_enemy:
                print("Your health: ", green + str(player["Hit Points"]) + default, "Enemy health: ",red + str(enemyhealth)+ default) 

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("Player health: ", player["Hit Points"], "Enemy health: ", enemyhealth)
            print("Congratulations,", player["name"] +"! You destroyed the robot", robot.upper())
            print("You are the winner! Enter any key to continue!")
            input()
            cls()
            return True
        else:
            player["Alive"] = False
            print("Player health: ", player["Hit Points"], "Enemy health: ", enemyhealth)
            print("Oh no the robot", robot.upper(), "destroyed you! Better luck next time. Press any key to continue.")
            input()
            cls()
            return False

        print("\nWould you like to play again?")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            again = False

#fighting()
