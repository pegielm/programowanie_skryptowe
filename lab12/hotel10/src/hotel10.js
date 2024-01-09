
const ADDroom = (number, limit, price) => {
    fetch('http://localhost:8000/addroom', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            number: number,
            limit: limit,
            price: price
        })
    }).then( res => res.json())
    .then(data => {
        if (data.status === 'OK') {
            window.alert('Room added');
        } else {
            window.alert('Error');
        }
    })
    .catch(err => console.trace(err));
}

let rooms = [];

const drawRooms = () => {
    var root = document.getElementById('rooms');
    for (let room of rooms) {
        var div = document.createElement('div');
        div.className = 'col-md-4';

        var img = document.createElement('img');
        img.className = 'room_image';
        img.src = `../public/images/${room.number}.jpg`;
        div.appendChild(img);

        var div2 = document.createElement('div');
        div2.className = 'card-body';

        var h5 = document.createElement('h5');
        h5.className = 'card-title';
        h5.textContent = `Pokój numer ${room.number}`;

        var ul = document.createElement('ul');
        ul.className = 'list-group list-group-flush list-unstyled';

        var li1 = document.createElement('li');
        li1.textContent = `Cena: ${room.price}zł`;

        var li2 = document.createElement('li');
        var free = room.limit - room.guests.length;
        li2.textContent = `Ilość wolnych miejsc: ${free}`;

        var button = document.createElement('button');
        var number = room.number;
        if (free == 0) {
            button.className = 'btn-room-full';
            button.onclick = function() {
                window.alert('Brak wolnych miejsc');
            }
        } else {
            button.className = 'btn-room';
            button.onclick = function() {
                var name = window.prompt('Podaj imię');
                var surname = window.prompt('Podaj nazwisko');
                var arrival = new Date(window.prompt('Podaj datę przyjazdu'));
                var departure = new Date(window.prompt('Podaj datę wyjazdu'));
                book(number, name, surname, arrival, departure);
                window.location.reload();
            }
        }
        button.textContent = 'Zarezerwuj';

        div.appendChild(button);
        div2.appendChild(h5);
        ul.appendChild(li1);
        ul.appendChild(li2);
        div2.appendChild(ul);
        div.appendChild(div2);
                                    
        root.appendChild(div);           
    }
}

fetch('/rooms')
    .then(response => response.json())
    .then(data => {rooms = data; drawRooms()})
    .catch(err => console.trace(err));

let reservations = [] 

fetch('/reservations')
    .then(response => response.json())
    .then(data => {reservations = data})
    .catch(err => console.trace(err));

          
// eslint-disable-next-line
const hotel = (commands) => {
    commands = commands.split(" ");
    
    let name;
    let surname;

    switch (commands[0].toLowerCase()) {
        case 'book':
            // eslint-disable-next-line
            const number = parseInt(commands[1]);
            name = commands[2];
            surname = commands[3];
            // eslint-disable-next-line
            const arrival = new Date(commands[4]);
            // eslint-disable-next-line
            const departure = new Date(commands[5]);
            book(number, name, surname, arrival, departure);            
            break;
        case 'guests':
            guests();
            break;
        case 'guest':
            name = commands[1];
            surname = commands[2];
            guest(name, surname);
            break;
        case 'hotel':
            hotel_print();
            break;
        case 'delete':
            fetch('http://localhost:8000/delete', 
            {
                method: 'POST'              
            })
            .then(res => res.json())
            .then(data => { console.log(data); })
            break;
        default:
            window.alert('Invalid command');
            break;
    }
    document.getElementById('command_console').value = '';
}

const book = (number, name, surname, arrival, departure) => {
    const room = rooms.find(room => {console.log(number, room.number); return room.number === number})
    console.group('book');
    if (room) {
        if (room.guests.length < room.limit) {                                                            
            console.log('Room Number:', number);
            console.log('Guest Name:', name + " " + surname);
            console.log('Arrival:', arrival);
            console.log('Departure:', departure);

            var time_diff = departure.getTime() - arrival.getTime();
            var days_past = time_diff / (1000 * 60 * 60 * 24);
            var price = days_past * room.price;
            console.log(`Price: ${price}`);

            fetch('http://localhost:8000/book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    number: number,
                    name: name,
                    surname: surname,
                    arrival: arrival,
                    departure: departure,
                    price: price
                })
            }).then( res => res.json())
            .then(data => {
                console.log(data);
                reservations.push(data);
            })
            .catch(err => console.trace(err));            
        } else {
            console.warn('Room is full');
        }
    } else {
        console.warn('Room not found');
    }
    console.groupEnd();
}

const guests = () => {
    console.group('guests');
    let guestlist = []
    for (const room of rooms) {
        guestlist = [...guestlist, ...room.guests]
    }
    guestlist = [...new Set(guestlist)];
    console.log(guestlist);
    console.groupEnd();
}

const guest = (name, surname) => {
    console.group('guest: ', `${name} ${surname}`);
    for (const room of rooms) {
        if (room.guests.includes(`${name} ${surname}`)) {                              
            console.log(`Room ${room.number} is rented by ${name} ${surname}`);
        }
    }
    var to_pay = 0;
    for (const reservation of reservations) {
        if (reservation.guest === `${name} ${surname}`) {
            to_pay = to_pay + parseInt(reservation.price);
        }
    }
    console.log(`To pay: ${to_pay}`)
    console.groupEnd(); 
}

const print_room = (number) => {
    for (const room of rooms) {
        if (room.number === number) {
            console.group('Room number:', number);
            console.log('Guests:', room.guests);
            console.log('Limit:', room.limit);
            console.log('Price:', room.price);
            console.groupEnd();
        }
    }
}

const hotel_print = () => {
    console.group('hotel');
    for (const room of rooms) {
        print_room(room.number);
    }
    console.groupEnd();
}

