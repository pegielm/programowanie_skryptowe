import json
import sys

def rooms(data):
    print("-------------+--------+--------+ ")
    print("Numer pokoju | Goście | Termin |")
    print("-------------+--------+--------+")
    for room in data:
        print(f"{room['number']}",end="")
        for i in range(1,room["space"]+1):
            if i == 1:
                print("",end="")
            else:
                print(" ",end="")
            print(f"            {i}. ",end="")
            try:
                print(f"{room['guests'][i-1]['name']} {room['guests'][i-1]['from']}-{room['guests'][i-1]['to']}")
            except IndexError:
                print("")
def show(data,guests):
    
    for guest in guests:
        resoult = []
        flag = False
        for room in data:
            for i in range(1,room["space"]+1):
                try:
                    if room["guests"][i-1]["name"] == guest:
                        flag = True
                        resoult.append({"room":room["number"],"from":room["guests"][i-1]["from"],"to":room["guests"][i-1]["to"]})
                        #print(f"{room['guests'][i-1]['from']}-{room['guests'][i-1]['to']}| {room['number']}")
                except IndexError:
                    print("",end="")
        if flag:
            print(f"{guest}")
            print("---------------------+------------")
            print("Termin               | Numer pokoju")
            print("---------------------+------------")
            for res in resoult:
                print(f"{res['from']}-{res['to']}| {res['room']}")
        else:
            print("Brak rezerwacji")

def book(data,rezervations):
    for rezervation in rezervations:
        try:
            guest = rezervation.split("|")[0]
            dates = rezervation.split("|")[1].split(":")
        except IndexError:
            print("zly format")
            return
        for date in dates:
            try:
                arrival = date.split("-")[0]
                departure = date.split("-")[1]
                room_number = departure.split("(")[1]
                room_number = room_number.split(")")[0]
                departure = departure.split("(")[0]
            except IndexError:
                print("zly format")
                return
            #print(f" guest: {guest} arrival: {arrival} departure: {departure} room_number: {room_number}")
            try:
                if len(data[int(room_number)-1]["guests"]) == data[int(room_number)-1]["space"]:
                    print("brak miejsc")
                    return
            
                data[int(room_number)-1]["guests"].append({"name":guest,"from":arrival,"to":departure})
            except IndexError:
                print("zly numer pokoju")
                return
            #print(data[int(room_number)-1]["guests"])
    with open(sys.argv[1], "w") as file:
        json.dump(data,file,indent=4)

def clear(data):
    for room in data:
        room["guests"] = []
    with open(sys.argv[1], "w") as file:
        json.dump(data,file,indent=4)

    
        
if __name__ == '__main__':
    try:
        with open(sys.argv[1], "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("zly plik")
        sys.exit(1)

    while True:
        try:
            command = input('>')
            command = command.split()
            if command[0] == 'rooms':
                rooms(data)
            elif command[0] == 'show':
                guests = command[1]
                show(data,guests)
            elif command[0] == 'book':
                reservations = command[1:]
                book(data,reservations)
            elif command[0] == 'clear':
                clear(data)
            else:
                print("zla komenda")
        except EOFError:
            break
"""
book a|01.01.2000-05.01.2000(1):05.01.2000-10.01.2000(2) b|22.12.2022-23.12.2023(3):23.12.2022-30.12.2022(4)
rooms
show a
show b
show c
book d|01.02.2022-01.03.2022(1)
"""

    


        

     



