import express from 'express';
import morgan from 'morgan';

/* *************************** */
/* Configuring the application */
/* *************************** */
const app = express();
const PORT = 8000;

// Set the view engine to Pug
app.set('view engine', 'pug');
app.use(express.static('static'));


// The resulting HTML code will be indented in the development environment
app.locals.pretty = app.get('env') === 'development';

/* ************************************************ */

app.use(express.urlencoded({ extended: true })); // Parse URL-encoded bodies for form data
app.use(morgan('dev'));

/* ******** */
/* "Routes" */
/* ******** */

const user = { description: 'User', authorised: false };
// Define a route for the home page
app.get('/', (request, response) => {
    let students = [
        {
              fname: 'Jan',
              lname: 'Kowalski'
        },
        {
              fname: 'Anna',
              lname: 'Nowak'
        },
    ];
    response.render('template' , {students, user}); // Render the 'template2' view with a default name
});

app.get('/submit', (request, response) => {
    response.send(`Hello ${request.query.name}`); // Send a response with the name from the query string')
});

app.post('/', (request, response) => {
    response.send(`Hello ${request.body.name}`); // Send a response with the name from the request body
});
// Start the server
app.listen(PORT, () => {
    console.log(`The server was started on port ${PORT}`);
    console.log('To stop the server, press "CTRL + C"');
});
