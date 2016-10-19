import random
from dictionaries import *
from items import *
names = ['Office',"Cupboard","Dungeon","Dark Room","Cave","Freezer","Kitchen","Mysterious Room","Messy Room"]

# A list of the 9 rooms on a floor. Each room has a name, description (maybe), exits (adjacent rooms), a boolean determining whether there are stairs,
# items and possibly a monster.

room_1 = {
    "name": "",

    "description":""" """,

    "exits": {"east":2 , "south":4},

    "items": [],

    "up": False,

    "monster": None
}

room_2 = {
    "name": "",

    "description":""" """,

    "exits": {"west": 1 , "south":5 , "east":3},

    "items": [],

    "up": False,

    "monster": None
}

room_3 = {
    "name": "",

    "description":""" """,

    "exits": {"west": 2 , "south":6},

    "items": [],

    "up": False,

    "monster": None
}

room_4 = {
    "name": "",

    "description":""" """,

    "exits": {"north": 1 , "east":5 , "south":7},

    "items": [],

    "up": False,

    "monster": None
}

room_5 = {
    "name": "",

    "description":""" """,

    "exits": {"west": 4,"south":8 , "east":6, "north":2},

    "items": [],

    "up": False,

    "monster": None
}

room_6 = {
    "name": "",

    "description":""" """,

    "exits": {"west": 5,"south":9,"north":3},

    "items": [],

    "up": False,

    "monster": None
}

room_7 = {
    "name": "",

    "description":""" """,

    "exits": {"north": 4,"east":8},

    "items": [],

    "up": False,

    "monster": None
}

room_8 = {
    "name": "",

    "description":""" """,

    "exits": {"west": 7,"north":5,"east":9},

    "items": [],

    "up": False,

    "monster": None
}

room_9 = {
    "name": "",

    "description":""" """,

    "exits": {"west": 8,"north":6},

    "items": [],

    "up": False,

    "monster": None
}





rooms = [
    room_1,
    room_2,
    room_3,
    room_4,
    room_5,
    room_6,
    room_7,
    room_8,
    room_9
]
# list of all rooms on a floor

def generate_floor(floor_number):
    # randomly generates a floor of 9 (3x3) rooms
    for r in rooms:
        r["up"] = False
        r["items"] = []
        x = random.randrange(0,30)
        if x <2:
            r["items"].append(Potion())
        elif x < 3:
            val = random.randrange(floor_number ,floor_number+5)
            r["items"].append(Equipment(val, weapon_names,adjectives,"ATT"))
        elif x < 4:
            val = random.randrange(floor_number ,floor_number+5)
            r["items"].append(Equipment(val, armour,adjectives,"DEF"))
        x = random.randrange(0,20)
        if x < 3:
            r["monster"] = True
    for r in rooms:
        i = random.randrange(0,len(names))
        r["name"] = names[i]

    j = random.randrange(0,9)
    rooms[j]["up"] = True

def print_map(current_room, name):
    """
    prints out a 3x3 grid of the rooms on the current floor.
    each room has 4 variables - items, monsters, the player and stairs.
    uses the first letter of the user's name as an icon 
    """
    output = ""
    print("\033[1;37;40m"+"┌─────┬─────┬─────┐")
    for i in range(0,3):
        a = [" "]*4
        b = [" "]*4
        c = [" "]*4
        row = [a, b, c]
        for index, s in enumerate(row):
            if current_room == rooms[(i*3) + index]:
                s[0] = name[0].upper()
            if rooms[(i*3) + index]["up"]:
                s[1] = "\033[1;32;40m"+ "▓" + "\033[1;37;40m"
            if rooms[(i*3) + index]["monster"] != None:
                s[2] = "\033[1;33;40m"+"!"+"\033[1;37;40m"
            if rooms[(i*3) + index]["items"] != []:
                s[3] = "\033[1;34;40m"+"¤"+"\033[1;37;40m"
        print("│ "+a[0]+" "+a[1]+" │ "+b[0]+" "+b[1]+" │ "+c[0]+" "+c[1]+" │")
        print("│ "+a[2]+" "+a[3]+" │ "+b[2]+" "+b[3]+" │ "+c[2]+" "+c[3]+" │")
        if i != 2:
            print("├─────┼─────┼─────┤")
        else:
            print("└─────┴─────┴─────┘" + "\033[1;37;40m")

generate_floor(1)

