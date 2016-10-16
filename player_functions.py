import math.random
# Work in Progress!

player = {"name" : player_name, "Hit Points" : current_health, "Max Hit Points" : max_health, "alive" : True, "EXP" : current_exp, "EXP to next level" : to_next_level, "level" : 1, "Attack Points" : atk, "Defense Points" : def_p}
# Values for the player, should be self explanatory.

def	player_gen(name="player"):
	player_name = name
	max_health = 13 + random.randint(1,13)
	current_health = max_health
	current_exp = 0
	to_next_level = 12
	atk = 5 + random.randint(1,10)
	def_p = 0 + random.randint(1,5)
	return
# This function is called once at the start of the game and assigns semi-random points to each variable. Feel free to change the points to create a better game balance when we get there, they are basically arbitrary.
# The player's name is taken for the scoreboard, but should default to player if left blank

def player_update(dmg = 0, heal = 0, xp = 0):
	current_health -= dmg
	current_health += heal
	if current_health <= 0:
		player["alive"] = False
	else if current_health > max_health:
		current_health = max_health
	current_exp += xp
	if current_exp >= to_next_level:
		level_up()
	return
# This function should be called when the players temporary stats need to be updated, such as when in combat or using a healing item

def level_up():
	hp = player["level"] + random.randint(0, player["level"])
	current_health += hp
	max_health += hp
	atk += player["level"] + random.randint(0, (player["level"]/2).floor())
	def_p += player["level"] + random.int(0, (player["level"]/4).floor())
	player["level"] = player["level"] + 1