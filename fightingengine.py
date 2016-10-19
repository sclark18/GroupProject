import math
import random
import collections

unsortedplayer = (("Name", ""),
          ("Health", 100),
          ("Alive" , True),
          ("XP", 0),
          ("XP to Level Up", 30),
          ("Level", 1),
          ("Attack Points", 5 + random.randint(1,10)))

player = collections.OrderedDict(unsortedplayer)

#def player_update(playerchoice, enemychoice, xp = 0):
	#player["Health"] -= playerchoice
	#player["Health"] += enemychoice
	#if player["Health"] <= 0:
		#player["Alive"] = False
	#if player["XP"] >= player["XP to Level Up"]:
		#level_up()
	#return
# This function should be called when the players temporary stats need to be updated, such as when in combat or using a healing item
# There should be no change in values when parameters are not entered

def level_up():
	hp = player["Level"] + random.randint(0, player["Level"])
	player["Health"] += hp
	player["Attack Points"] += player["Level"] + random.randint(0, (math.floor(player["Level"]/2)))
	player["Level"] = player["Level"] + 1
	player["XP"] = round((player["XP to Level Up"] + player["XP"]*random.uniform(0,1)), 0)
	player["XP to Level Up"] = player["Level"] + player["XP to Level Up"]*2
	return
    
def print_stats():
    for key, value in player.items():
        print(key + ":", value)
        
def update_xp(playerchoice):
    xp = playerchoice * random.randint(0,1)
    print(xp)

def main():
    player["Name"] = input("What is your name: ").capitalize()
    print("Welcome to the game,", player["Name"])
    print("----------------------------------------------------------------")
    print("                         HOW TO PLAY")
    print("----------------------------------------------------------------")
    print("")
    print("Fight against the computer in an battle using a range of atacks")
    print("Different types of attack will do various ammounts of damage")
    print("You can also choose to skip the attack and heal")
    print("After each sucessful attack you will gain attack points and EXP")
    print("These points will help you level up")
    print("Any move you make can miss, so choose wisely!")
    print("----------------------------------------------------------------")
    print("")
    print_stats()

    again = True

    # Set up the play again loop
    while again:

    
        winner = None
        player["Health"] = 100
        enemyhealth = 100

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            turn_player = True
            turn_enemy = False
            print("")
            print("------------------")
            print("You will go first.")
            print("------------------")
        else:
            turn_player = False
            turn_enemy = True
            print("")
            print("------------------")
            print("Your enemy will go first.")
            print("------------------")
        print("Your health: ", player["Health"])
        print("Enemy health: ", enemyhealth)

        #main game loop
        while (player["Health"] != 0 or enemyhealth != 0):
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
                print("4. Heal (Heal by 20-30")
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
                        elif player["Health"] > 35 and player["Health"] <= 75:
                            move_choice = ["Punch", "Kick", "Karate Chop"]
                            move_choice = random.choice(move_choice)
                            enemychoice = moves[move_choice]
                            print("Your enemy used", move_choice, "Damage:", enemychoice)
                        elif player["Health"] <= 35:
                            enemychoice = moves["Kick"]
                            print("Your enemy kicks you to the floor! Damage:", enemychoice)                     
                    else: # if the computer has less than 30 health, there is a 50% chance they will heal
                        choice5050 = random.randint(1,2) 
                        if choice5050 == 1:
                            heal = True
                            enemychoice = moves["Heal"]
                            print("Your enemy chose to heal. Their health increaed to ", enemychoice)
                        else:
                            if player["Health"] > 75:
                                enemychoice = moves["Punch"]
                                print("Your enemy lands a hard punch right on your nose! Damage:", enemychoice)
                            elif player["Health"] > 35 and player["Health"] <= 75:
                                move_choice = ["Punch", "Kick", "Karate Chop"]
                                move_choice = random.choice(move_choice)
                                enemychoice = moves[move_choice]
                                print("Your enemy used ", move_choice, ". Damage:", enemychoice)
                            elif player["Health"] <= 35:
                                enemychoice = moves["Kick"] 
                                print("Your enemy kicked you. Ouch! Damage:", enemychoice)

            if heal:
                if turn_player:
                    player["Health"] += playerchoice
                    
                    if player["Health"] > 100:
                        player["Health"] = 100 # cap max health at 100. No over healing!
                        
                else:
                    enemyhealth += enemychoice
                    if enemyhealth > 100:
                        enemyhealth = 100
            else:
                if turn_player:
                    enemyhealth -= playerchoice
                    xp = (playerchoice*random.uniform(0,1))
                    xp = round(xp, 0)
                    player["XP"] = round(player["XP"] + xp, 0)
                    if enemyhealth < 0:
                        enemyhealth = 0 # cap minimum health at 0
                        winner = "Player"
                        break
                else:
                    player["Health"] -= enemychoice
                    if player["Health"] < 0:
                        player["Health"] = 0
                        winner = "Enemy"
                        break
            if player["XP"] >= player["XP to Level Up"]:
                print("Level Up!!")
                level_up()
                if player["Health"] > 100:
                    player["Health"] = 100
                print("-----------------------")   
                print_stats()
                print("-----------------------")
            print("Your health: ", player["Health"], "Enemy health: ", enemyhealth)


            # switch turns
            turn_player = not turn_player
            turn_enemy = not turn_enemy

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("Player health: ", player["Health"], "Enemy health: ", enemyhealth)
            print("Congratulations,", player["Name"] +"! You won!!")
        else:
            player["Alive"] = False
            print("Player health: ", player["Health"], "Enemy health: ", enemyhealth)
            print("Sorry, but you lost. Better luck next time.")

        print("\nWould you like to play again?")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            again = False

main()
