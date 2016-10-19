import math
import random
import collections
from player_functions import *
from dictionaries import *

def print_stats():
        print("Name:", player["name"])
        print("Hit Points:", player["Hit Points"])
        print("Alive:", player["alive"])
        print("EXP:", player["EXP"])
        print("EXP to next level:", player["EXP to next level"])
        print("Current Level:", player["level"])
        print("Attack points:", player["Attack Points"])
        print("Defense points:", player["Defense Points"])

def fighting():
    robotgen = list(robots.keys())
    robot_fight = (random.choice(robotgen))
    print("Oh no! A robot",robot_fight, "appeared!")
    print("-----------------------")
    winner = None
    player["Hit Points"] = 13 + random.randint(1,13)
    enemyhealth = 2*player["level"] + random.randint(1,2*player["level"])

    print("Try to defeat the",robot_fight,"with a variety of attacks")
    print("You can also choose to skip the attack and heal")
    print("After each sucessful attack you will gain attack points and EXP")
    print("These points will help you level up")
    print("Any move you make can miss, so choose wisely!")
    print("----------------------------------------------------------------")
    print("")
    # you can get rid of the instructions when adding to main game if you want ^
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
    print("Your health: ", player["Hit Points"])
    print("Enemy health: ", enemyhealth)
    while (player["Hit Points"] != 0 or enemyhealth != 0):
        heal = False
        miss = False
        moves = {"Punch": random.randint(1,5),
                 "Kick": random.randint(2,6),
                 "Karate Chop": random.randint(1,7),
                 "Heal": random.randint(5,12)}
        if turn_player:
                print("You can: ")
                print("1. Punch (1-5 damage)")
                print("2. Kick (2-6 damage)")
                print("3. Karate Chop (1-7 damage)")
                print("4. Heal (Heal by 5-12)")
                print("5. View stats")
                print("-----------------------")
                
                playerchoice = input("Select a move: ").lower()
                print("-----------------------")
                chance_of_miss = random.randint(1,5) # 1 in 5 chance player misses

                if chance_of_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    dmg = 0 # player misses and deals no damage
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
                    print("The computer missed!")
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
                     if player["Hit Points"] > 100:
                        player["Hit Points"] = 100 # cap max health at 100. No over healing!
                        
                else:
                    enemyhealth += enemychoice
                    if enemyhealth > 100:
                        enemyhealth = 100
        else:
                if turn_player:
                        enemyhealth = enemyhealth - playerchoice
                        xp = (playerchoice*random.uniform(0.1,1))
                        xp = round(xp, 0)
                        player["EXP"] = round(player["EXP"] + xp, 0)
                        if enemyhealth < 0:
                                enemyhealth = 0 # cap minimum health at 0
                                winner = "Player"

                else:
                        player["Hit Points"] = player["Hit Points"] - enemychoice
                        if player["Hit Points"] < 0:
                                player["Hit Points"] = 0
                                winner = "Enemy"

        if player["EXP"] >= player["EXP to next level"]:
                print("Level Up!!")
                level_up()
                if player["Hit Points"] > 100:
                    player["Hit Points"] = 100
                print("-----------------------")   
                print_stats()
                print("-----------------------")
        print("Your health: ", player["Hit Points"], "Enemy health: ", enemyhealth)
        # switch turns
        turn_player = not turn_player
        turn_enemy = not turn_enemy

        if winner == "Player":
            print("Player health: ", player["Hit Points"], "Enemy health: ", enemyhealth)
            print("Congratulations,", player["name"] +"! You destroyed the", robot_fight)
            break
        elif winner == "Enemy":
            player["Alive"] = False
            print("Player health: ", player["Hit Points"], "Enemy health: ", enemyhealth)
            print("Oh no the", robot_fight, "destroyed you! Better luck next time.")
            break
        else:
            continue



fighting()
