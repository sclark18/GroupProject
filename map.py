import random
names = ['Big_room',"Small_room","Not_a_room","Nice_room","Better_room","Room_of_rooms","The_room","Final_room","Tahano_room"]

room_1 = {
    "name": "",

    "description":""" """,

    "exits": {"east": "Second" , "south":"Fourth"},

    "items": []
}

room_2 = {
    "name": "",

    "description":""" """,

    "exits": {"west": "First" , "south":"Fifth" , "east":"Third"},

    "items": []
}

room_3 = {
    "name": "",

    "description":""" """,

    "exits": {"west": "Second" , "south":"Sixth"},

    "items": []
}

room_4 = {
    "name": "",

    "description":""" """,

    "exits": {"north": "First" , "east":"Fifth" , "south":"Seventh"},

    "items": []
}

room_5 = {
    "name": "",

    "description":""" """,

    "exits": {"west": "Fourth","south":"Eight" , "east":"Sixth", "north":"Second"},

    "items": []
}

room_6 = {
    "name": "",

    "description":""" """,

    "exits": {"west": "Fifth","south":"Nineth","north":"Third"},

    "items": []
}

room_7 = {
    "name": "",

    "description":""" """,

    "exits": {"north": "Fourth","east":"Eight"},

    "items": []
}

room_8 = {
    "name": "",

    "description":""" """,

    "exits": {"west": "Seventh","north":"Fifth","east":"Nineth"},

    "items": []
}

room_9 = {
    "name": "",

    "description":""" """,

    "exits": {"west": "Eight","north":"Sixth"},

    "items": []
}





rooms = {
    "First": room_1,
    "Second": room_2,
    "Third": room_3,
    "Fourth": room_4,
    "Fifth": room_5,
    "Sixth": room_6,
    "Seventh": room_7,
    "Eight": room_8,
    "Nineth": room_9
}


for key in rooms:
    # do something with value
    name = random.choice(names)
    rooms[key]["name"] = name
    names.remove(name)
