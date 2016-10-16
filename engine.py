#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from removeing import *
import random
import time



def list_of_items(items):
    listofitems = []
    for i in items:
    	listofitems.append(i["name"])

    str1 = ", ".join(listofitems)
    return str1



def print_room_items(room):
    var = list_of_items(room["items"])
    if var != "":
        print("There is "+var+" here.")
        print()





def print_inventory_items(items):
    print("You have" , list_of_items(inventory) +".") #passed
    print()




def print_room(room):
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)
    #
    # COMPLETE ME!
    #



def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]




def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")




def print_menu(exits, room_items, inv_items):
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))

    for i in room_items:
    	print("TAKE " + (i["id"]).upper() +" to take a "+(i["name"])+".")

    for i in inv_items:
        print("DROP " + (i["id"]).upper() +" to drop your "+(i["name"])+".")

    print("What do you want to do?")




def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits




def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"] , direction):
        current_room = move(current_room["exits"] , direction)




def execute_take(item_id):
    for item in current_room["items"]:
        if item["id"]==item_id:
            inventory.append(item)
            current_room["items"].remove(item)
            return
    print("you cannot take that")
    



def execute_drop(item_id):
    for item in inventory:
        if item["id"]==item_id:
            inventory.remove(item)
            current_room["items"].append(item)
            return
    print("you cannot drop that")
 
def execute_kill(mob):
    mob = 0
    print(mob)


def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "kill":
        if len(command) > 1:
            execute_kill(command[1])
        else:
            print("Kill what?")


    else:
        print("This makes no sense.")




def menu(exits, room_items, inv_items):
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input




def move(exits, direction):
    return rooms[exits[direction]]




def main():
    # Main game loop
    t1 = time.strftime("%H:%M:%S")
    (h, m, s) = t1.split(':')
    resone = int(h) * 3600 + int(m) * 60 + int(s)

    while True:
        end = 0
        x = 10 #SETTIN THE TIME(in seconds)
        while (end < x):
            t2 = time.strftime("%H:%M:%S")
            (h, m, s) = t2.split(':')
            result = int(h) * 3600 + int(m) * 60 + int(s)
            end = result - resone
            disp = x - end
            print()
            print()
            if disp > 0:
                print('You have' , disp , "seconds left.")
            elif disp <= 0:
                break # if we want the last command to be accepted delete break and write sg else instead
            # Display game status (room description, inventory etc.)
            print_room(current_room)
            print_inventory_items(inventory)

            # Show the menu with possible actions and ask the player
            command = menu(current_room["exits"], current_room["items"], inventory)

            # Execute the player's command
            execute_command(command)
        print("Sorry your time is over.")
        break



if __name__ == "__main__":
    main()

