import datetime
import sys
import json
import time
import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)
logging.info('Started')

class User:
    def __init__(self, name):
        self.name = name
        self.groups = ""
        if self.name == "admin" or self.name == "michal":
            self.group = "admin"
        else:
            self.group = "user"
    
class AccessError(Exception):
    pass

data_name = sys.argv[1]
user_name = sys.argv[2]
current_user = User(user_name)


def user(group):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if group == current_user.group or current_user.group == "admin":
                return func(*args, **kwargs)
            else:
                raise AccessError("Access denied")
        return wrapper
    return decorator

def log_to(file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.info(f'{datetime.datetime.now()} user: {current_user.name} wywolal funkcje {func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator
'''
def log_to(file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                open(file, 'a')
            except FileNotFoundError:
                sys.touch(file)
            with open(file, 'a') as f:
                f.write(f'{datetime.datetime.now()} user: {current_user.name} wywolal funkcje {func.__name__}')
                for arg in args:
                    f.write(f'{arg} ')
                f.write('\n')
            return func(*args, **kwargs)
        return wrapper
    return decorator'''

class Room:
    def __init__(self, numer, ilosc_miejsc, cena):
        self.numer = numer
        self.ilosc_miejsc = ilosc_miejsc
        self.cena = cena

    def __str__(self):
        return f"Numer: {self.numer}\nMaksymalna liczba osób: {self.ilosc_miejsc}\nCena: {self.cena} zł\n"
    
    def __repr__(self):
        return f"Numer: {self.numer} Ilosc miejsc: {self.ilosc_miejsc} Cena: {self.cena}"

class Guest:
    def __init__(self, imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def __repr__(self):
        return f"{self.imie} {self.nazwisko}"
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
    def __eq__(self, other):
        self.imie == other.imie and self.nazwisko == other.nazwisko
    def __hash__(self):
        return hash((self.imie, self.nazwisko))
class Reservation:
    def __init__(self, room, check_inDate, check_outDate):
        self.room:Room = room
        self.check_inDate:datetime = check_inDate
        self.check_outDate:datetime = check_outDate
    def __str__(self):
        return f"{self.room} {self.check_inDate} {self.check_outDate}"
    def __repr__(self):
        return f"{self.room} {self.check_inDate} {self.check_outDate}"
    
class Hotel:
    rooms = []
    def __init__(self):
        self.guests: dict[Guest, list[Reservation]] = {}
    @user('admin')
    @log_to("log.txt")
    def book(self,guest, room_number, check_inDate, check_outDate):
        for room in self.rooms:
            if room.numer == room_number:
                if room.ilosc_miejsc >= len(self.guests):
                    reservation = Reservation(room, check_inDate, check_outDate)
                    if guest in self.guests:
                        self.guests[guest].append(reservation)
                    else:
                        self.guests[guest] = [reservation]
                    print("Zarezerwowano pokój")
                else:
                    print("Nie można zarezerwować pokoju")
    @log_to("log.txt")
    def show_room(self, room_number):
        for room in self.rooms:
            if room.numer == room_number:
                print(room)
                for guest in self.guests:
                    for reservation in self.guests[guest]:
                        if reservation.room == room:
                            print(guest )
                            print(reservation)
    @user('michal')
    @log_to("log.txt")
    def show_guests(self):
        for guest in self.guests:
            print(guest)

    @user('michal')        
    @log_to("log.txt")        
    def show_guest(self,imie,nazwisko):
        for guest in self.guests.keys():
            if guest.imie == imie and guest.nazwisko == nazwisko:
                print(guest)
                for reservation in self.guests[guest]:
                    print(reservation)
    def add_reservation(self, guest, reservation):
        if guest in self.guests.keys():
            self.guests[guest].append(reservation)
        else:
            self.guests[guest] = [reservation]
    def print_reservations(self):
        for guest in self.guests:
            print(guest)
            for reservation in self.guests[guest]:
                print(reservation)
    
    




hotel = Hotel()
''' hotel.rooms.append(Room(1,2,100))
hotel.rooms.append(Room(2,2,100))
hotel.rooms.append(Room(3,3,150))
hotel.add_reservation(Guest("Jan","Kowalski"),Reservation(hotel.rooms[0],datetime.datetime(2021,5,1),datetime.datetime(2021,5,10)))
hotel.add_reservation(Guest("Adam","Jakis"),Reservation(hotel.rooms[1],datetime.datetime(2021,5,1),datetime.datetime(2021,5,10)))'''
with open(data_name, "r") as file:
    data = json.load(file)
    for room in data:
        hotel.rooms.append(Room(room["numer"],room["miejsce"],room["cena"]))
        current = hotel.rooms[-1]
        for guest in room["guests"]:
            hotel.add_reservation(Guest(guest["imie"],guest["nazwisko"]),Reservation(current,datetime.datetime.strptime(guest["od"], '%d-%m-%Y'),datetime.datetime.strptime(guest["do"], '%d-%m-%Y')))
            print(guest["imie"],guest["nazwisko"],room["numer"],guest["od"],guest["do"])
while True:
    try:
        command = input('>')
        command = command.split(" ")
        if command[0] == 'rooms':
            print(hotel.rooms)
        elif command[0] == 'room':
            try:
               hotel.show_room(int(command[1])) 
            except IndexError:
                print("Błąd: Nie ma takiego pokoju")
        elif command[0] == 'guests':
            hotel.show_guests()
        elif command[0] == 'book':
            try:         
                hotel.book(Guest(command[1],command[2]),int(command[3]),datetime.datetime.strptime(command[4], '%d-%m-%Y'),datetime.datetime.strptime(command[5], '%d-%m-%Y'))
            except IndexError:
                print("Błąd: Nie ma takiego gościa lub pokoju")
            except ValueError:
                print("Błąd: Zły format daty")
        elif command[0] == 'guest':
            try:
                hotel.show_guest(command[1],command[2])
            except IndexError:
                print("Błąd: Nie ma takiego gościa")
        elif command[0] == 'reservations':
            hotel.print_reservations()
        elif command[0] == 'help':
            print("rooms - wyświetla listę pokoi")
            print("room <numer> - wyświetla informacje o pokoju")
            print("guests - wyświetla listę gości")
            print("book <imie> <nazwisko> <numer_pokoju> <%d-%m-%Y> <%d-%m-%Y> - rezerwuje pokój")
            print("exit - wychodzi z programu")
        elif command[0] == 'exit':
            break
    except EOFError:
        break