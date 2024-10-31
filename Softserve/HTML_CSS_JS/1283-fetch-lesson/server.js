const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
app.use(express.json());
app.use(express.static(path.resolve(__dirname, './')));
app.listen(process.env.PORT || 3000, process.env.IP || '0.0.0.0');

app.get('/api/chat', (req, res) => {
    const data = fs.readFileSync('./chat.txt', { encoding: 'utf-8', flag: 'r' });
    res.send({ data });
});

app.post('/api/chat', (req, res) => {
    fs.appendFile('./chat.txt', req.body.message + '\n', err => {
        if (err) {
            res.send(500).send('Server Error');
        }
        const data = fs.readFileSync('./chat.txt', { encoding: 'utf-8', flag: 'r' });
        res.send({ data });
    })
});
