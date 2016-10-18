#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from removeing import *
import random
import time
from player_functions import *

floornumber = 1

disp = 0

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
    global current_room
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))

    for i in room_items:
    	print("TAKE " + (i["id"]).upper() +" to take a "+(i["name"])+".")

    for i in inv_items:
        print("DROP " + (i["id"]).upper() +" to drop your "+(i["name"])+".")

    if current_room["up"] == 'yes':
        print("NEXT FLOOR to go to the next floor.")

    print("Write TIME to check how much time you spent.")

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


def execute_nextfloor():
    global floornumber
    names = ['Big_room',"Small_room","Not_a_room","Nice_room","Better_room","Room_of_rooms","The_room","Final_room","Tahano_room"]
    floornumber = floornumber + 1
    floorup = ["f","a","s","d","yes","g","h","i","j"]
    player["EXP"] = player["EXP"] + floornumber


    print("------------------------------------------------------------------------------")
    print("           You have sucesfully entered to the floor number",floornumber,"!")
    print("------------------------------------------------------------------------------")

    for key in rooms:
        # do something with value
        name = random.choice(names)
        rooms[key]["name"] = name
        names.remove(name)

    for key in rooms:
        # do something with value
        up = random.choice(floorup)
        rooms[key]["up"] = up
        floorup.remove(up)

    for key in rooms:
        rooms[key]["items"] = []




def execute_command(command):
    global disp
    global current_room
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

    elif command[0] == "next":
        if len(command) > 1:
            if current_room["up"]=="yes":
                execute_nextfloor()
        else:
            print("Which floor?")

    elif command[0] == "time":
        if len(command) > 1:
            print('You have' , disp , "seconds left.")
        else:
            print('You have' , disp , "seconds left.")






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
    print()
    player_gen(input("What is your name explorer?"))
    print("Welcome",player["name"],"to the game.")
    print("Let the game begin. You are in the :")
    global disp
    # Main game loop
    t1 = time.strftime("%H:%M:%S")
    (h, m, s) = t1.split(':')
    resone = int(h) * 3600 + int(m) * 60 + int(s)
    while player["alive"] == True:
        end = 0
        x = 0 #SETTIN THE TIME(in seconds)
        t2 = time.strftime("%H:%M:%S")
        (h, m, s) = t2.split(':')
        result = int(h) * 3600 + int(m) * 60 + int(s)
        end = result - resone
        disp = end - x 

        # if we want the last command to be accepted delete break and write sg else instead
        # Display game status (room description, inventory etc.)    
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)
        
    



if __name__ == "__main__":
    main()

