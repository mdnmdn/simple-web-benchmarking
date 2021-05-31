const { promisify } = require("util");
const express = require('express')
const redis = require("redis");
const app = express()
const port = process.env.PORT || 3000

const l = console.log;

const redisClient = redis.createClient({ host: 'redis' });
redisClient.asyncIncr = promisify(redisClient.incr).bind(redisClient);

const randomKey = () => `key_${(Math.random() * 200).toFixed(0)}`;

app.get('/', (req, res) => {
  res.send('ok - express');
});

app.get('/redis/incr', async (req, res) => {
  const key = randomKey();
  const val = await redisClient.asyncIncr(key);
  res.send(`express: ${key}: ${val}`);
})

app.listen(port, () => {
  l(`Example app listening at http://localhost:${port}`)
});

