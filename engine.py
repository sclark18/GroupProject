#!/usr/bin/python3

from map import *
from player import *
from items import *
from removeing import *
import random
import time
from player_functions import *
from fightingengine import *
from scoreboard import *
import os


floornumber = 1
# the current floor. used in scores
timeshow = 0
disp = 0

def cls():
    # clears the screen
    os.system('cls' if os.name=='nt' else 'clear')


def list_of_items(items):
    # returns a string representation of a list of items
    listofitems = []
    for i in items:
        listofitems.append(i.get_full_name())

    str1 = ", ".join(listofitems)
    return str1 + "."



def print_room_items(room):
    # prints the items within the room
    var = list_of_items(room["items"])
    if var != ".":
        print("Items in this room: ")
        print("\033[1;34;40m" + var + "\033[1;37;40m")


def print_inventory_items(items):
    # prints the items in the player's inventory
    print_equipment()
    print("Potions: " + str(player["Inventory"]))
    print()

def print_equipment():
    output = "You are equipped with: \n"
    if player["Weapon"] != None:
        output += ("a " + player["Weapon"].get_full_name() + "\n")
    if player["Armour"] != None:
        output += ("a " + player["Armour"].get_full_name())
    print(output)

def print_stats():
    pass


def print_room(room):
    # prints the current room's name and description, along with a map showing the room's location and other information
    print()
    print(room["name"].upper())
    print_map(room,player["name"])
    print(room["description"])
    print()
    print_room_items(room)
    



def exit_leads_to(exits, direction):
    # returns the room that a chosen exit refers to
    if is_valid_exit(exits,direction):
        return rooms[(exits[direction]-1)]




def print_exit(direction, leads_to):
    # prints the name of an adjacent room in a given direction
    print("GO " + direction.upper() + " to " + leads_to + ".")




def print_menu(exits, room_items, inv_items):
    #prints the game menu
    global current_room

    if current_room["up"] == True:
        print("\033[1;32;40m" + "NEXT FLOOR to go to the next floor." + "\033[1;37;40m")

    print("What next?")




def is_valid_exit(exits, chosen_exit):
    # returns true if there is an exit in a given direction; false otherwise
    return chosen_exit in exits




def execute_go(direction):
    # moves the player if possible, prints a notification if otherwise
    global current_room
    if is_valid_exit(current_room["exits"] , direction):
        current_room = rooms[(current_room["exits"][direction]-1)]
    else:
        print("You cannot go that way...")


def execute_drop(item_pre, item_name):
    # drops an item from inventory
    if player["Weapon"].name.lower() == item_pre + " " + item_name:
        current_room["items"].append(player["Weapon"])
        player["Weapon"] = None
    elif player["Armour"].name.lower() == item_pre + " " + item_name:
        current_room["items"].append(player["Armour"])
        player["Armour"] = None
    else:
        print("You cannot drop that...")

def execute_take(item_pre, item_name):
    # equips an item
    for item in current_room["items"]:
        if item.__class__ == Potion:
            player["Inventory"] += 1
            current_room["items"].remove(item)
        elif item.name.lower()==item_pre + " " + item_name:
            if item.__class__ == Equipment:
                if item.type == "ATT":
                    x = equip_weapon(item)
                    if x != None:
                        current_room["items"].append(x)
                else:
                    x = equip_armour(item)
                    if x != None:
                        current_room["items"].append(x)
                current_room["items"].remove(item)
            return
    print("you cannot equip that")
 
def execute_drink():
    if player["Inventory"] > 0:
        if player["Hit Points"] == player["Max Hit Points"]:
            print("You are already at full health!")
            return
        player["Inventory"] -= 1
        player_update(0,30,0)
    else:
        print("You have no more potions left!")


def execute_nextfloor():
    # generates a new floor and gives the player some exp
    global floornumber
    floornumber = floornumber + 1
    player["EXP"] = player["EXP"] + floornumber

    print("\033[1;32;40m")
    print("------------------------------------------------------------------------------")
    print("           You have sucesfully entered floor ",floornumber,"!")
    print("------------------------------------------------------------------------------")
    print("\033[1;37;40m")
    generate_floor(floornumber)




def execute_command(command):
    # executes the user's command
    global disp
    global current_room
    cls()
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 2:
            execute_take(command[1], command[2])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 2:
            execute_drop(command[1], command[2])
        else:
            print("Drop what?")


    elif command[0] == "next":
        if len(command) > 1:
            if current_room["up"]== True:
                execute_nextfloor()
        else:
            print("Which floor?")

    elif command[0] == "time":
        global timeshow
        timeshow = 1

    elif command[0] == "drink":
        execute_drink()

    elif command[0] == "equip":
        if len(command) > 2:
            execute_equip(command[1],command[2])
        else:
            print("Equip What?")


def menu(exits, room_items, inv_items):
    # displays the game menu and returns the user's (normalised) input
    print_menu(exits, room_items, inv_items)
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def main():
    cls()
    print("\033[1;37;40m")
    print("Welcome to K.I.R.I.L.L!")
    print("Robots are invadeing the Tower of London")
    print("Your duty is to destroy as much as you can in five minutes.")
    print("You can use the following commands:")
    print("DROP to drop an item from your inventory.")
    print("TAKE to pick up an item from a room.")
    print("NEXT FLOOR to go to the next floor")
    print("TIME to chech how much time you have left.")
    print("DRINK to drink an owned potion")
    print("GO <direction> to move.")
    print("Good Luck!")
    print("")

    player_gen(input("What is your name explorer? "))
    print("Welcome to the game, ",player["name"],".")
    print("Let the game begin. You are in the :")
    # clears the screen, asks for the user's name and welcomes them
    global timeshow
    global disp
    t1 = time.strftime("%H:%M:%S")
    (h, m, s) = t1.split(':')
    resone = int(h) * 3600 + int(m) * 60 + int(s)
    # initializes timer
    disp = 1 #comparizon
    timecheck = 120 # SETTING THE TIME(in seconds)
    while player["alive"] == True:
        while disp > 0 :
            # game loop
            end = 0
            t2 = time.strftime("%H:%M:%S")
            (h, m, s) = t2.split(':')
            result = int(h) * 3600 + int(m) * 60 + int(s)
            disp = timecheck + resone -result
            




            # if we want the last command to be accepted delete break and write sg else instead
            # Display game status (room description, inventory etc.) 
            if current_room["monster"] == True:
                x = fighting()
                if not x:
                    player["alive"] = False
                    break
                else:
                    current_room["monster"] = None
            print_room(current_room)
            if timeshow == 1:
                 if disp > 0:
                    a = int(disp / 60)
                    b = disp % 60 
                    timeshow = 0
                    print('You have' , a , "minutes and",b,"seconds left")
            print_inventory_items(inventory)

            # Show the menu with possible actions and ask the player
            command = menu(current_room["exits"], current_room["items"], inventory)

            # Execute the player's command
            execute_command(command)
        print("Your time is over")
        print("Saveing your score...")
        address = "scores"
        data = process_file(address)
        save_data(address,data,floornumber,player["name"])
        data = process_file(address)
        print_scoreboard(data)
        print("Your score is saved!")
        print("Press a key to exit.")
        input()
        cls()
        print("\033[1;37;40m")
        break
        
    



if __name__ == "__main__":
    main()

