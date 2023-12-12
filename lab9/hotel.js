var db;
var request = indexedDB.open("BazaHotelowa", 1);

request.onupgradeneeded = function(event) {
    db = event.target.result;
    var pokojeMagazyn = db.createObjectStore("pokoje", { keyPath: "numer" });
    var goscieMagazyn = db.createObjectStore("goscie", { keyPath: "id", autoIncrement: true });
    var rezerwacjeMagazyn = db.createObjectStore("rezerwacje", { autoIncrement: true });
};

request.onsuccess = function(event) {
    db = event.target.result;
};

function wykonaj() {
    var polecenieInput = document.getElementById("text").value;
    var czesci = polecenieInput.split(" ");

    switch (czesci[0]) {
        case "wynajmij":
            if (!czesci[1] || isNaN(parseInt(czesci[1])) || !czesci[2] || isNaN(parseInt(czesci[2])) || !czesci[3] || isNaN(parseInt(czesci[3]))) {
                console.error("Błąd: Wszystkie argumenty muszą być prawidłowymi liczbami.");
            } else {
                wynajmijPokojDlaGoscia(parseInt(czesci[1]), parseInt(czesci[2]), parseInt(czesci[3]));
            }
        break;
        case "listaGosci":
            wyswietlListeGosci();
            break;
        case "wykazWynajec":
            if (!czesci[1] || isNaN(parseInt(czesci[1]))) {
                console.error("Błąd: ID gościa musi być prawidłową liczbą.");
            } else {
                wykazWynajec(parseInt(czesci[1]));
            }
            break;
        case "stanHotelu":
            wyswietlStanHotelu();
            break;
        case "dodajPokoj":
            if (!czesci[1] || isNaN(parseInt(czesci[1])) || !czesci[2] || isNaN(parseInt(czesci[2])) || !czesci[3] || isNaN(parseInt(czesci[3]))) {
                console.error("Błąd: Wszystkie argumenty muszą być prawidłowymi liczbami.");
            } else {
                dodajPokoj(parseInt(czesci[1]), parseInt(czesci[2]), parseInt(czesci[3]));
            }
            break;
        case "dodajGosc":
            if (!czesci[1] || !czesci[2]) {
                console.error("Błąd: Imię i nazwisko gościa są wymagane.");
            } else {
                dodajGosc(czesci[1], czesci[2]);
            }
            break;;
        case "dostepnePokoje":
            wyswietlDostepnePokoje();
            break;
        case "rezerwacje":
            wyswietlRezerwacje();
            break;
        case "wyczysc":
            if (!db) {
                console.warn("Ostrzeżenie: Baza danych nie istnieje.");
            } else {
                db.close();
                indexedDB.deleteDatabase("BazaHotelowa");
                console.warn("Baza danych została wyczyszczona");
            }
            break;
        case "pokoj":
            if (!czesci[1] || isNaN(parseInt(czesci[1]))) {
                console.error("Błąd: Numer pokoju musi być prawidłową liczbą.");
            } else {
               wyswietlPokoj(parseInt(czesci[1]));
            }
            break;
        case "pomoc":
            console.group("Pomoc");
            console.log("wynajmij [idGoscia] [numerPokoju] [iloscDni]");
            console.log("listaGosci");
            console.log("wykazWynajec [idGoscia]");
            console.log("stanHotelu");
            console.log("dodajPokoj [numer] [pojemnosc] [cena]");
            console.log("dodajGosc [imie] [nazwisko]");
            console.log("dostepnePokoje");
            console.log("rezerwacje");
            console.log("pomoc");
            console.groupEnd("Pomoc");
            break;
        default:
            console.warn("Nieznane polecenie");
    }
}

function wynajmijPokojDlaGoscia(idGoscia, numerPokoju, iloscDni) {
    var transakcja = db.transaction(["pokoje", "rezerwacje", "goscie"], "readwrite");
    var pokojeMagazyn = transakcja.objectStore("pokoje");
    var rezerwacjeMagazyn = transakcja.objectStore("rezerwacje");
    var goscieMagazyn = transakcja.objectStore("goscie");

    var zapytaniePokoju = pokojeMagazyn.get(numerPokoju);
    zapytaniePokoju.onsuccess = function(event) {
        var pokoj = event.target.result;

        if (pokoj && pokoj.iloscMiejsc > 0) {
            pokoj.iloscMiejsc--;
            pokojeMagazyn.put(pokoj);

            var rezerwacja = { numerPokoju: numerPokoju, iloscDni: iloscDni, idGoscia: idGoscia };
            rezerwacjeMagazyn.add(rezerwacja);

            var zapytanieGoscia = goscieMagazyn.get(idGoscia);
            zapytanieGoscia.onsuccess = function(goscEvent) {
                var gosc = goscEvent.target.result;

                if (gosc) {
                    gosc.rezerwacja = { numerPokoju: numerPokoju, iloscDni: iloscDni };
                    goscieMagazyn.put(gosc);
                }
            };

            console.group("Wynajęcie pokoju");
            console.log("Numer pokoju:", numerPokoju);
            console.log("Ilość dni:", iloscDni);
            console.log("ID gościa:", idGoscia);
            console.groupEnd();

            console.log("Pokój wynajęty na", iloscDni, "dni dla gościa o ID:", idGoscia);
        } else {
            console.error("Nie można wynająć pokoju o numerze", numerPokoju);
        }
    };
}

function wyswietlListeGosci() {
    var transakcja = db.transaction(["goscie"], "readonly");
    var goscieMagazyn = transakcja.objectStore("goscie");

    console.group("Lista gości");
    var zapytanieKursora = goscieMagazyn.openCursor();
    zapytanieKursora.onsuccess = function(event) {
        var kursor = event.target.result;
        if (kursor) {
            console.log("Gość:", kursor.key ,kursor.value.imie, kursor.value.nazwisko);
            kursor.continue();
        } else {
            console.groupEnd();
        }
    };
}

function wykazWynajec(idGoscia) {
    var transakcja = db.transaction(["rezerwacje"], "readonly");
    var rezerwacjeMagazyn = transakcja.objectStore("rezerwacje");

    console.group("Rezerwacje dla gościa o ID:", idGoscia);
    var zapytanieKursora = rezerwacjeMagazyn.openCursor();
    zapytanieKursora.onsuccess = function(event) {
        var kursor = event.target.result;
        if (kursor) {
            if (kursor.value.idGoscia === idGoscia) {
                console.log("Rezerwacja:", "Pokój", kursor.value.numerPokoju, "na", kursor.value.iloscDni, "dni");
            }
            kursor.continue();
        } else {
            console.groupEnd();
        }
    };
}

function wyswietlStanHotelu() {
    var transakcja = db.transaction(["pokoje", "goscie"], "readonly");
    var pokojeMagazyn = transakcja.objectStore("pokoje");
    var goscieMagazyn = transakcja.objectStore("goscie");
    var zapytanieLiczbyPokoi = pokojeMagazyn.count();
    zapytanieLiczbyPokoi.onsuccess = function(event) {
        var liczbaWolnychPokoi = event.target.result;
    
        var zapytanieLiczbyGosci = goscieMagazyn.count();
        zapytanieLiczbyGosci.onsuccess = function(event) {
            var liczbaGosci = event.target.result;
    
            console.group("Stan hotelu");
            console.log("Liczba pokoi:", liczbaWolnychPokoi);
            console.log("Liczba gości:", liczbaGosci);
            console.groupEnd();
        };
    };
}

function dodajPokoj(numer, pojemnosc, cena) {
    var transakcja = db.transaction(["pokoje"], "readwrite");
    var pokojeMagazyn = transakcja.objectStore("pokoje"); 
    var nowyPokoj = { numer: numer, iloscMiejsc: pojemnosc, cena: cena };
    var dodajPokojZapytanie = pokojeMagazyn.add(nowyPokoj);
    dodajPokojZapytanie.onsuccess = function(event) {
    console.group("Dodano nowy pokój");
    console.log("ID", event.target.result);
    console.log("Numer pokoju:", numer);
    console.log("Pojemność:", pojemnosc);
    console.log("Cena:", cena);
    console.groupEnd();
    };
}

function dodajGosc(imie, nazwisko) {
    var transakcja = db.transaction(["goscie"], "readwrite");
    var goscieMagazyn = transakcja.objectStore("goscie");
    var nowyGosc = { imie: imie, nazwisko: nazwisko };

    var dodajGoscZapytanie = goscieMagazyn.add(nowyGosc);
    dodajGoscZapytanie.onsuccess = function(event) {
        console.group("Dodano nowego gościa");
        console.log("ID:", event.target.result);
        console.log("Imię:", imie);
        console.log("Nazwisko:", nazwisko);
        console.groupEnd();
    };
}

function wyswietlDostepnePokoje() {
    var transakcja = db.transaction(["pokoje"], "readonly");
    var pokojeMagazyn = transakcja.objectStore("pokoje");
    console.group("Dostępne pokoje");
    var zapytanieKursora = pokojeMagazyn.openCursor();
    zapytanieKursora.onsuccess = function(event) {
        var kursor = event.target.result;
        if (kursor) {
            console.log("Pokój:", kursor.value.numer, "pojemność:", kursor.value.iloscMiejsc, "cena:", kursor.value.cena);
            kursor.continue();
        } else {
            console.groupEnd();
        }
    };

}

function wyswietlRezerwacje() {
    var transakcja = db.transaction(["rezerwacje", "goscie"], "readonly");
    var rezerwacjeMagazyn = transakcja.objectStore("rezerwacje");
    var goscieMagazyn = transakcja.objectStore("goscie");
    console.group("Rezerwacje");
    var zapytanieKursora = rezerwacjeMagazyn.openCursor();
    zapytanieKursora.onsuccess = function(event) {
    var kursor = event.target.result;
    if (kursor) {
        var zapytanieGoscia = goscieMagazyn.get(kursor.value.idGoscia);
        zapytanieGoscia.onsuccess = function(goscEvent) {
            var gosc = goscEvent.target.result;
            console.log("Rezerwacja:", "Pokój", kursor.value.numerPokoju, "dla", gosc.imie, gosc.nazwisko, "na", kursor.value.iloscDni, "dni");
            kursor.continue();
        };
    } else {
        console.groupEnd();
    }
    };
}

function wyswietlPokoj(numer) {
    var transakcja = db.transaction(["rezerwacje", "goscie"], "readonly");
    var rezerwacjeMagazyn = transakcja.objectStore("rezerwacje");
    var goscieMagazyn = transakcja.objectStore("goscie");

    console.group("Rezerwacje dla pokoju numer:", numer);
    var zapytanieKursora = rezerwacjeMagazyn.openCursor();
    zapytanieKursora.onsuccess = function(event) {
        var kursor = event.target.result;
        if (kursor) {
            if (kursor.value.numerPokoju === numer) {
                var zapytanieGoscia = goscieMagazyn.get(kursor.value.idGoscia);
                zapytanieGoscia.onsuccess = function(goscEvent) {
                    var gosc = goscEvent.target.result;
                    console.log("Gość:", gosc.imie, gosc.nazwisko, "na", kursor.value.iloscDni, "dni");
                };
            }
            kursor.continue();
        } else {
            console.groupEnd();
        }
    };
}



