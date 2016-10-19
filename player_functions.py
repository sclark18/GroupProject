import math
import random
from items import *
# Work in Progress!

player = { 
"name" : "", 
"Hit Points" : 0, 
"Max Hit Points" : 0, 
"alive" : True, 
"EXP" : 0, 
"EXP to next level" : 0, 
"level" : 1, 
"Attack Points" : 0, 
"Defense Points" : 0,
"Inventory":1, 
"Weapon" : Equipment(1,["Sword"],["Basic"],"ATT"), 
"Armour" : Equipment(1,["Shirt"],["White"],"DEF")
}
# Values for the player, should be self explanatory.
# When displaying the amount of EXP to the next level to the player, it should be player["EXP to next level"] - player["EXP"]

def player_gen(name="player"):
	player["name"] = name
	player["Max Hit Points"] = 13 + random.randint(1,13)
	player["Hit Points"] = player["Max Hit Points"]
	player["EXP"] = 0
	player["EXP to next level"] = 12
	player["Attack Points"] = 5 + random.randint(1,10)
	player["Defense Points"] = 0 + random.randint(1,5)
	return
# This function is called once at the start of the game and assigns semi-random points to each variable. Feel free to change the points to create a better game balance when we get there, they are basically arbitrary.
# The player's name is taken for the scoreboard, but should default to player if left blank

def player_update(dmg = 0, heal = 0, xp = 0):
	player["Hit Points"] -= dmg
	player["Hit Points"] += heal
	if player["Hit Points"] <= 0:
		player["alive"] = False
	elif player["Hit Points"] > player["Max Hit Points"]:
		player["Hit Points"] = player["Max Hit Points"]
	player["EXP"] += xp
	if player["EXP"] >= player["EXP to next level"]:
		level_up()
	return
# This function should be called when the players temporary stats need to be updated, such as when in combat or using a healing item
# There should be no change in values when parameters are not entered

def level_up():
	hp = player["level"] + random.randint(0, player["level"])
	player["Hit Points"] += hp
	player["Max Hit Points"] += hp
	player["Attack Points"] += player["level"] + random.randint(0, (math.floor(player["level"]/2)))
	player["Defense Points"] += player["level"] + random.randint(0, (math.floor(player["level"]/4)))
	player["level"] = player["level"] + 1
	player["EXP"] = player["EXP to next level"] - player["EXP"]
	player["EXP to next level"] = player["level"] + player["EXP to next level"] + 12
	return
# This function is called by player_update when the player is due to level up
# This could be updated later in development to print the player's updated stats and allow the player more choice in which stats are upgraded
# The stat upgrades are all prospective and fairly arbitrary and you should all feel free to change them for better game balance when we get there

def equipment_update(item):
    if item.type == "ATT":
        player["Attack Points"] += item.val
    elif item.type == "DEF":
        player["Defense Points"] += item.val
#this function edits the players stats according to the items that are currently equipped

def equipment_gen(item):
    item_stats = random.randint(1,(player["level"]))       
    item.update({"Defense Points" : item_stats})
    return
# This function will take an input from the dictionaries.py dictionary and assign integer stats to them according to the player's stats
# This function is to be used on equipment

def weapon_gen(item):
    item_stats = random.randint(1,(player["level"]))       
    item.update({"Attack Points" : item_stats})
    return
# Same as equipment_gen() but for weapons

def equip_weapon(item):
	if player["Weapon"] == None:
		player["Weapon"] = item
	else:
		a = player["Weapon"]
		player["Weapon"] = item
		return a


def equip_armour(item):
	if player["Armour"] == None:
		player["Armour"] = item
	else:
		a = player["Armour"]
		player["Armour"] = item
		return a
	
# These functions should edit the player's equipped set and change their stats accordingly
# These functions are also untested
        

# This function is called whenever the inventory is changed and necessary changes will be saved

""" I used these tests to check these functions worked and it looked alright to me so it should be in working order.
player_gen()

print(player)

player_update(2,0,0)

print(player)

player_update(xp = 12)

print(player)

input("enter to exit!!!")
"""
