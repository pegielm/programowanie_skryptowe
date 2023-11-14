import datetime
class Hotel:
    rooms = []
    def __init__(self):
        self.reservations: list[Reservation]= []
    def book(self, pesel, room_number, check_inDate, check_outDate):
        pesel_exists = False
        room_exists = False
        new_guest = None
        new_room = None
        for reservation in self.reservations:
            if reservation.guest.pesel == pesel:
                pesel_exists = True
                new_guest = reservation.guest
        for room in self.rooms:
            if room.numer == room_number:
                if room.ilosc_miejsc < 1:
                    print("Pokój jest zajęty")
                    return
                room_exists = True
                new_room = room
        if pesel_exists == False:
            print("Dodawanie  nowego goscia")
            imie = input("Podaj imie: ")
            nazwisko = input("Podaj nazwisko: ")
            new_guest = Guest(imie, nazwisko, pesel)
        if room_exists == False:
            print("Dodawanie nowego pokoju")
            numer = input("Podaj numer pokoju: ")
            ilosc_miejsc = input("Podaj ilosc miejsc: ")
            cena = input("Podaj cene: ")
            self.rooms.append(Room(numer, ilosc_miejsc, cena))
        if room_exists and pesel_exists:
            self.reservations.append(Reservation(new_guest, new_room, check_inDate, check_outDate))
            new_room.ilosc_miejsc -= 1
    def add_reservation(self, reservation):
        self.reservations.append(reservation)
        self.rooms.append(reservation.room)
        
    def show_room(self, room_number):
        for room in self.rooms:
            if room.numer == room_number:
                print(room)
                for reservation in self.reservations:
                    if reservation.room.numer == room_number:
                        print(reservation)

    def show_guests(self):
        for reservation in self.reservations:
            print(reservation.guest)
    def show_guest(self, pesel):
        for reservation in self.reservations:
            if reservation.guest.pesel == pesel:
                print(reservation.guest)
                print(reservation)
class Reservation:
    def __init__(self, guest, room, check_inDate, check_outDate):
        self.guest:Guest = guest
        self.room:Room = room
        self.check_inDate:datetime = check_inDate
        self.check_outDate:datetime = check_outDate
    def __str__(self):
        return f"{self.guest} {self.room} {self.check_inDate} {self.check_outDate}"
    def __repr__(self):
        return f"{self.guest}"
    
    
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
    def __init__(self, imie,nazwisko,pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
    def __repr__(self):
        return f"{self.imie} {self.nazwisko}"
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

if __name__ == "__main__":
    hotel = Hotel()
    hotel.add_reservation(Reservation(Guest("Jan", "Janowski", "1"), Room(1, 0, 150), datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 10)))
    hotel.add_reservation(Reservation(Guest("Anna", "Anielska", "2"), Room(2, 1, 250), datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 10)))
    hotel.add_reservation(Reservation(Guest("Bartek", "Bartoszewski", "3"), Room(3, 2, 200), datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 10)))
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
                print(hotel.reservations)
            elif command[0] == 'book':
                try:         
                   # pesel room_number check_inDate check_outDate
                    pesel = command[1]
                    room_number = int(command[2])
                    check_inDate = datetime.datetime.strptime(command[3], '%d-%m-%Y')
                    check_outDate = datetime.datetime.strptime(command[4], '%d-%m-%Y')
                    hotel.book(pesel, room_number, check_inDate, check_outDate)
                except IndexError:
                    print("Błąd: Nie ma takiego gościa lub pokoju")
                except ValueError:
                    print("Błąd: Zły format daty")
            elif command[0] == 'guest':
                try:
                    hotel.show_guest(command[1])
                except IndexError:
                    print("Błąd: Nie ma takiego gościa")
            elif command[0] == 'help':
                print("rooms - wyświetla listę pokoi")
                print("room <numer> - wyświetla informacje o pokoju")
                print("guests - wyświetla listę gości")
                print("book <pesel> <numer> <check_inDate> <check_outDate> - rezerwuje pokój")
                print("exit - wychodzi z programu")
            elif command[0] == 'exit':
                break

        except EOFError:
            break