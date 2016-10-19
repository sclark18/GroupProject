#!/usr/bin/python3

from map import *
from player import *
from items import *
from removeing import *
import random
import time
from player_functions import *
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
        print("There is "+var+" here.")
        print()






def print_inventory_items(items):
    # prints the items in the player's inventory
    print("You have" , list_of_items(inventory) +".") #passed
    print()




def print_room(room):
    # prints the current room's name and description, along with a map showing the room's location and other information
    print()
    print(room["name"])
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
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction)["name"])

    for i in room_items:
    	print("TAKE " + (i["id"]).upper() +" to take a "+(i["name"])+".")

    for i in inv_items:
        print("DROP " + (i["id"]).upper() +" to drop your "+(i["name"])+".")

    if current_room["up"] == True:
        print("NEXT FLOOR to go to the next floor.")

    print("Write TIME to check how much time you have left.")

    print("What do you want to do?")




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




def execute_take(item_pre, item_name):
    # takes an item from the current room
    for item in current_room["items"]:
        if item.name.lower()==item_pre + " " + item_name:
            inventory.append(item)
            current_room["items"].remove(item)
            return
    print("you cannot take that")
      



def execute_drop(item_pre, item_name):
    # drops an item from inventory
    for item in inventory:
        if item.name.lower() == item_pre + " " + item_name:
            inventory.remove(item)
            current_room["items"].append(item)
            return
    print("you cannot drop that")
 
def execute_kill(mob):
    # kills a monster
    mob = 0
    print(mob)


def execute_nextfloor():
    # generates a new floor and gives the player some exp
    global floornumber
    floornumber = floornumber + 1
    player["EXP"] = player["EXP"] + floornumber


    print("------------------------------------------------------------------------------")
    print("           You have sucesfully entered to the floor number",floornumber,"!")
    print("------------------------------------------------------------------------------")

    generate_floor()




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
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 2:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "kill":
        if len(command) > 1:
            execute_kill(command[1])
        else:
            print("Kill what?")

    elif command[0] == "next":
        if len(command) > 1:
            if current_room["up"]== True:
                execute_nextfloor()
        else:
            print("Which floor?")

    elif command[0] == "time":
        global timeshow
        timeshow = 1


def menu(exits, room_items, inv_items):
    # displays the game menu and returns the user's (normalised) input
    print_menu(exits, room_items, inv_items)
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def main():
    cls()
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
    timecheck = 300 # SETTING THE TIME(in seconds)
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
        #saveing the score command
        print("Your score is saved!")
        print("Press a key to exit.")
        input()
        break
        
    



if __name__ == "__main__":
    main()

