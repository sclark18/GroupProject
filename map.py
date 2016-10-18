import random
names = ['Big_room',"Small_room","Not_a_room","Nice_room","Better_room","Room_of_rooms","The_room","Final_room","Tahano_room",]

floorup = ["f","a","s","d","yes","g","h","i","j"]

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


"""for key in rooms:
    # do something with value
    name = random.choice(names)
    rooms[key]["name"] = name
    names.remove(name)

for key in rooms:
    # do something with value
    up = random.choice(floorup)
    rooms[key]["up"] = up
    floorup.remove(up)
"""
def generate_floor():
    for r in rooms:
        r["up"] = False
        r["items"] = []
    for r in rooms:
        i = random.randrange(0,len(names))
        r["name"] = names[i]

    j = random.randrange(0,9)
    rooms[j]["up"] = True

def print_map(current_room):
    output = ""
    print("┌─────┬─────┬─────┐")
    for i in range(0,3):
        a = [" "]*4
        b = [" "]*4
        c = [" "]*4
        row = [a, b, c]
        for s in row:
            ind = row.index(s)
            if current_room == rooms[(i*3) + ind]:
                s[0] = "P"
            if rooms[(i*3) + ind]["up"]:
                s[1] = "^"
            if rooms[(i*3) + ind]["monster"] != None:
                s[2] = "X"
            if rooms[(i*3) + ind]["items"] != []:
                s[3] = "I"
        print("│ "+a[0]+" "+a[1]+" │ "+b[0]+" "+b[1]+" │ "+c[0]+" "+c[1]+" │")
        print("│ "+a[2]+" "+a[3]+" │ "+b[2]+" "+b[3]+" │ "+c[2]+" "+c[3]+" │")
        if i != 2:
            print("├─────┼─────┼─────┤")
        else:
            print("└─────┴─────┴─────┘")

        """output += "│"
        if r["up"]:
            output += "X"
        else:
            output += " "
        if r == current_room:
            output += "O"
        else:
            output += " "
        if r == room_3 or r == room_6 or r == room_9:
            print(output + "|")
            output = ""
"""
generate_floor()

