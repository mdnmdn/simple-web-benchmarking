const express = require('express')
const app = express()
const port = process.env.PORT || 3000

const l = console.log;

app.get('/', (req, res) => {
  res.send('ok - express');
})

app.listen(port, () => {
  l(`Example app listening at http://localhost:${port}`)
});

