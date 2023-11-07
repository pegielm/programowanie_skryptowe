import datetime

class Room:
    def __init__(self, numer, ilosc_miejsc, cena):
        self.numer = numer
        self.ilosc_miejsc = ilosc_miejsc
        self.cena = cena
        self.aktualna_liczba_osob = 0
        self.lista_gosci = []

    def __str__(self):
        data = f"Numer: {self.numer}\nMaksymalna liczba osób: {self.ilosc_miejsc}\nAktualna liczba osób: {self.aktualna_liczba_osob}\nCena: {self.cena} zł\n"
        wypisani = []
        for i in self.lista_gosci:
            for j in i.rezerwacje:
                if j["room"] == self.numer:
                    if i.imie not in wypisani:
                        data += f"{i.imie} {j['from']} - {j['to']}\n"
                        
            wypisani.append(i.imie)        
        return data

    def __repr__(self):
        return f"Numer: {self.numer} Aktualna liczba osób: {self.aktualna_liczba_osob}" 

class Guest:
    def __init__(self, imie):
        self.imie = imie
        self.rezerwacje = []
    def __repr__(self):
        return f"{self.imie}"
    def __str__(self):
        data = f"Imię: {self.imie}\n"
        for i in self.rezerwacje:
            data += f"Pokoj nr: {i['room']}   {i['from']}    {i['to']}\nDo zaplaty:{i['price']} zł\n"
        return data
    
    
    
    def book(self, room, start_date, end_date):
        if room.aktualna_liczba_osob + 1 <= room.ilosc_miejsc:
            room.aktualna_liczba_osob += 1
            cena = (end_date - start_date).days * room.cena
            self.rezerwacje.append({"room":room.numer, "from":start_date, "to":end_date, "price":cena})
            room.lista_gosci.append(self)
            print("sukces")
        else:
            print("error")

list_of_rooms = [
    Room(1, 3, 150),
    Room(2, 3, 250),
    Room(3, 2, 200),
]

list_of_guests = [
    Guest("Jan Kowalski"),
    Guest("Anna Kowalska" ),
    Guest("Joanna Bielecka"),
]
while True:
    try:
        command = input('>')
        command = command.split(" ")
        if command[0] == 'rooms':
            print(list_of_rooms)
        elif command[0] == 'room':
            try:
                print(list_of_rooms[int(command[1])])
            except IndexError:
                print("Błąd: Nie ma takiego pokoju")
        elif command[0] == 'guests':
            print(list_of_guests)
        elif command[0] == 'guest':
            try:
                print(list_of_guests[int(command[1])])
            except IndexError:
                print("Błąd: Nie ma takiego gościa")
        elif command[0] == 'book':
            try:
                guest = list_of_guests[int(command[1])]
                room = list_of_rooms[int(command[2])]
                start_date = datetime.datetime.strptime(command[3], "%d-%m-%Y")
                end_date = datetime.datetime.strptime(command[4], "%d-%m-%Y")
                guest.book(room, start_date, end_date)
            except IndexError:
                print("Błąd: Nie ma takiego pokoju lub gościa")
            except ValueError:
                print("Błąd: Zły format daty")
    except EOFError:
        break