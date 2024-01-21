import express from 'express';
import bodyParser from 'body-parser';
import fs from 'fs/promises';
import { MongoClient } from 'mongodb';

import { fileURLToPath } from 'url';
import { dirname } from 'path';
import { getSystemErrorMap } from 'util';
import { exit } from 'process';
import crsf from 'csurf';
import cookieParser from 'cookie-parser';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express(); //nie da s ie
app.use(cookieParser());
app.use(crsf({ cookie: true }));
app.use(express.static('public'));
app.use(function (req, res, next) {
    res.cookie('XSRF-TOKEN', req.csrfToken());
    next();
});

app.disable('x-powered-by');
app.use(function (err, req, res, next) {
    console.error(err.stack);
    res.status(500).send('Something broke!');
  });
const port = 8000;
const mongo_path = '';
if (mongo_path == '' ){
    console.error('MongoDB path is empty');
    exit(1);
}

app.use(bodyParser.json());

app.get('/src/hotel10.html', (req, res) => {
    res.sendFile('/src/hotel10.html', { root: __dirname });
});

app.get('/src/hotel10.js', (req, res) => {
    res.sendFile('/src/hotel10.js', { root: __dirname });
});



app.get('/login', async (req, res) => {
    console.log('GET');
    
    const USERlogin = req.query.login; 
    const USERpassword = req.query.password;

    console.log(USERlogin);
    console.log(USERpassword);

    try {
        const data = JSON.parse(await fs.readFile('./hotel10/public/passwd.json', 'utf8'));
        const user = data.find(user => user.id === USERlogin);
        console.log(user);
        if (user && user.password === USERpassword) {
            res.json({ status: 'OK' });
        } else {
            res.json({ status: 'ERROR' });
        }
    } catch (err) {
        console.trace(err);
        res.status(500).send('Server error');
    }
});

app.get('/rooms', async (req, res) => {
    const client = new MongoClient(mongo_path);
    await client.connect();
    console.log('Connected successfully to server - rooms');

    const db = client.db('HOTEL');
    const collection = db.collection('rooms');
    const data = await collection.find().toArray();
    console.log(data);
    client.close();
    res.json(data);
});

app.get('/reservations', async (req, res) => {
    const client = new MongoClient(mongo_path);
    await client.connect();
    console.log('Connected successfully to server - reservations');

    const db = client.db('HOTEL');
    const collection = db.collection('reservations');
    const data = await collection.find().toArray();
    client.close();
    res.json(data);
});

app.get('/public/images/1.jpg', (req, res) => {
    res.sendFile('/public/images/1.jpg', { root: __dirname });
});

app.get('/public/images/2.jpg', (req, res) => {
    res.sendFile('/public/images/2.jpg', { root: __dirname });
});

app.get('/public/images/3.jpg', (req, res) => {
    res.sendFile('/public/images/3.jpg', { root: __dirname });
});

app.post('/book', async (req, res) => {
    console.log('POST');
    
    try {
        const body = req.body;
        console.log(body);

        const reservation = {number: body.number, guest: `${body.name} ${body.surname}`, arrival: body.arrival, departure: body.departure, price: body.price};
        console.log('1 POST:', reservation);

        const client = new MongoClient(mongo_path);
        await client.connect();
        console.log('Connected successfully to server - POST');

        const db = client.db('HOTEL');
        const roomsDB = db.collection('rooms');
        const reservationsDB = db.collection('reservations');
        
        if (typeof body.number !== 'number' || body.number < 1 || body.number > 1000 || 
            typeof body.name !== 'string' || !body.name.match(/^[A-Za-z]+$/) ||
            typeof body.surname !== 'string' || !body.surname.match(/^[A-Za-z]+$/)) {
            console.error('Invalid input types');
            res.status(400).send('Invalid input');
            return;
        }
        ///jest rozwiazne wyzej
        await roomsDB.updateOne(
            { number: body.number },
            { $push: { guests: `${body.name} ${body.surname}`} }
        )

        await reservationsDB.insertOne(reservation, (insertErr, result) => {
            if (insertErr) {
              console.error('Error inserting document:', insertErr);
              res.status(500).send('Server error');
            }            
        });
        client.close();
        res.json(reservation);
        console.log(reservation);
    } catch (err) {
        console.trace(err);
        console.error('Error handling POST request:', err);
        res.status(500).send('Server error');
    }
});

app.post('/delete', async (req, res) => {
    console.log('POST');

    try {
        const client = new MongoClient(mongo_path);
        await client.connect();
        console.log('Connected successfully to server - DELETE');

        const db = client.db('HOTEL');
        const roomsDB = db.collection('rooms');
        const reservationsDB = db.collection('reservations');

        const roomIds = [101,102,201,203];

        await roomsDB.updateMany(
            { number: { $in: roomIds } },
            { $set: { guests: [] } },
            (updateErr, result) => {
              if (updateErr) {
                console.error('Error updating documents:', updateErr);
                res.status(500).send('Server error');
              }            
            }
        );
        await reservationsDB.deleteMany({}, (deleteErr, result) => {
            if (deleteErr) {
              console.error('Error deleting documents:', deleteErr);
            } else {
              console.log('Documents deleted successfully:', result.deletedCount);
            }
        });
        res.json('All data has been deleted');
        client.close();
    } catch (err) {
        console.trace(err);
        console.error('Error handling POST request:', err);
        res.status(500).send('Server error');
    }
});

app.post('/addroom', async (req, res) => {
    const body = req.body;
    console.log(body);
    
    if (body.number && body.limit && body.price) {
        const room = {number: parseInt(body.number), limit: parseInt(body.limit), price: parseInt(body.price), guests: []};
        try {
            const client = new MongoClient(mongo_path);
            await client.connect();
            console.log('Connected successfully to server - ADDROOM');

            const db = client.db('HOTEL');
            const roomsDB = db.collection('rooms');

            const result = await roomsDB.insertOne(room);
            console.log('Inserted document with _id:', result.insertedId);

            client.close();
        } catch (err) {
            console.trace(err);
            console.error('Error handling POST request:', err);
            res.status(500).send('Server error');
        }
    } else {
        console.log('Invalid data');
    }
});

app.get('/', (req, res) => {
    res.redirect('/src/hotel10.html');
});

app.listen(port, () => {
    console.log(`Listening at http://localhost:${port}`);
});