const express = require('express');
const app = express();
const mongoose = require('mongoose');
const db = require('./config/keys').mongoURI;
const bodyParser = require('body-parser');
const cors = require('cors')
require('dotenv/config')

const postsRoutes = require('./routes/posts');
const usersRoutes = require('./routes/users');

// middlewares
// just a funtion that executes that when routes are being hit
// app.use('/posts', ()=> {
//     console.log('this is a middleware logging me!')
// })
app.use(bodyParser.json())
app.use(cors())

app.use('/users', usersRoutes)
app.use('/posts', postsRoutes)

//routes
app.get('/', (req,res) =>{
    res.send('hello from ed')
})

// on browser remeber default is get routes
// app.get('/posts', (req,res) =>{
//     res.send('hello from posts')
// })

// use patch for deleting

// connect to the DB
mongoose.connect(process.env.DB_CONNECTION, { useUnifiedTopology: true, useNewUrlParser: true})
    .then( () => console.log('connected to mongo DB'))
    // .catch( err => console.log('DB connetion FAILED!\n'))
    .catch( err => console.log('DB connetion FAILED!\n', err))

// listen to a server
app.listen(3000)