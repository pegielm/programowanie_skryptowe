import json
import sys

with open("rooms.json", "r") as file:
    data = json.load(file)

def add_guest(room_number, guest_data):
    for room in data:
        if room["number"] == room_number:
            max_space = room["space"]
            if len(room["guests"]) < max_space:
                room["guests"].append(guest_data)
                return True
    return False
def remove_guest(room_number, guest_name):
    for room in data:
        if room["number"] == room_number:
            for guest in room["guests"]:
                if guest["name"] == guest_name:
                    room["guests"].remove(guest)
                    return True
def clear_room(room_number):
    for room in data:
        if room["number"] == room_number:
            room["guests"] = []
            return True
    return False

if sys.argv[-1] == "--clear":
    for room in data:
        clear_room(room["number"])
    with open("rooms.json", "w") as file:
        json.dump(data, file, indent=4)

for i in range(1, len(sys.argv)-1,3):
    try:
        int(sys.argv[i])
    except ValueError:
        print("numer pokoju musi byc liczba")
        sys.exit(1)
    try:
        sys.argv[i+1]
        sys.argv[i+2]
    except IndexError:
        print("nalezy podac imie i nazwisko goscia")
        sys.exit(1)
    if(sys.argv[i+1][0]=="-" or sys.argv[i+2][0]=="-"):
        print("niepoprawne imie lub nazwisko")
        sys.exit(1)
    
    guest_to_add = { "name": sys.argv[i+1], "surname": sys.argv[i+2] }
    
    
    if add_guest(int(sys.argv[i]), guest_to_add):
        print("gosc dodany")
    else:
        print("blad dodawania goscia")

    try:
        with open("rooms.json", "w") as file:
            json.dump(data, file, indent=4)
    except:
        print("blad zapisu do pliku")
        sys.exit(1)

if(sys.argv[-1]=="--stan_pokoi"):
    print("-------------+--------+")
    print("Numer pokoju | Goście |")
    print("-------------+--------+")
    for room in data:
        print(f"{room['number']}",end="")
        for i in range(1,room["space"]+1):
            if i == 1:
                print("",end="")
            else:
                print(" ",end="")
            print(f"          {i}. ",end="")
            try:
                print(f"{room['guests'][i-1]['name']} {room['guests'][i-1]['surname']}")
            except IndexError:
                print("")
        

     



