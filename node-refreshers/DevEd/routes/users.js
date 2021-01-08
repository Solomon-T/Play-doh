const express = require('express');

const router = express.Router();

router.get('/users', (req, res) => {
    res.send("We are on users' users")
})

router.get('/', (req, res) => {
    res.send('We are on users')
})

module.exports = router;