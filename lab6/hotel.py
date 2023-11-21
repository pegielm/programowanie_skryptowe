import datetime
class Hotel:
    rooms = []
    def __init__(self):
        self.guests: dict[Guest, list[Reservation]] = {}
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
    def show_room(self, room_number):
        for room in self.rooms:
            if room.numer == room_number:
                print(room)
    def show_guests(self):
        for guest in self.guests:
            print(guest)
    def show_guest(self,imie,nazwisko):
        for guest in self.guests:
            if guest.imie == imie and guest.nazwisko == nazwisko:
                print(guest)
                for reservation in self.guests[guest]:
                    print(reservation)
    def add_reservation(self, guest, reservation):
        if guest in self.guests:
            self.guests[guest].append(reservation)
        else:
            self.guests[guest] = [reservation]
class Reservation:
    def __init__(self, room, check_inDate, check_outDate):
        self.room:Room = room
        self.check_inDate:datetime = check_inDate
        self.check_outDate:datetime = check_outDate
    def __str__(self):
        return f"{self.room} {self.check_inDate} {self.check_outDate}"
    def __repr__(self):
        return f"{self.room} {self.check_inDate} {self.check_outDate}"
    
    
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

if __name__ == "__main__":
    hotel = Hotel()
    hotel.rooms.append(Room(1,2,100))
    hotel.rooms.append(Room(2,2,100))
    hotel.rooms.append(Room(3,3,150))
    hotel.add_reservation(Guest("Jan","Kowalski"),Reservation(hotel.rooms[0],datetime.datetime(2021,5,1),datetime.datetime(2021,5,10)))
    hotel.add_reservation(Guest("Adam","Jakis"),Reservation(hotel.rooms[1],datetime.datetime(2021,5,1),datetime.datetime(2021,5,10)))
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