import express from 'express';
import morgan from 'morgan';
import { MongoClient } from 'mongodb';

const app = express();
const PORT = 8000;
const user = { description: 'User', authorised: true };


app.set('view engine', 'pug');
app.locals.pretty = app.get('env') === 'development';

app.use(express.urlencoded({ extended: true }));
app.use(morgan('dev'));

const dbName = 'AGH';

app.get('/', (req, res) => {
    res.send(':)'); 
});

app.get('/:wydzial', async (req, res) => {
    const wydzial = req.params.wydzial;

    const client = new MongoClient('mongodb+srv://pegielm:qTe46DUQQVwXuNK@agh.bfrc6us.mongodb.net/?retryWrites=true&w=majority');
    await client.connect();
    const db = client.db(dbName);
    const collection = db.collection('students');
    const students = await collection.find({ wydzial: wydzial }).toArray();
    res.render('template', { students, user , wydzial});
    client.close(); 
});

app.listen(PORT, () => {
    console.log(`Serwer uruchomiony na porcie ${PORT}`);
    console.log('Aby zatrzymać serwer, naciśnij "CTRL + C"');
});
