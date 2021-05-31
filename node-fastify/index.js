const fastify = require('fastify')()

const port = process.env.PORT || 3000;


fastify.register(require('fastify-redis'), { host: 'redis' })


// fastify.register(require('fastify-postgres'), {
//   connectionString: 'postgres://postgres@localhost/postgres'
// })
// 
// fastify.get('/user/:id', async (req, reply) => {
//   const client = await fastify.pg.connect()
//   const { rows } = await client.query(
//     'SELECT id, username, hash, salt FROM users WHERE id=$1', [req.params.id],
//   )
//   client.release()
//   return rows
// })

const randomKey = () => `key_${(Math.random() * 200).toFixed(0)}`;

fastify.get('/', async (req, res) => {
  return 'ok - fastify';
});

fastify.get('/redis/incr', async (req, res) => {
  const key = randomKey();
  const { redis } = fastify;
  const val = await redis.incr(key);
  return `fastify: ${key}: ${val}`;
});


fastify.listen(port, '0.0.0.0', err => {
  if (err) throw err
  console.log(`server listening on ${fastify.server.address().port}`)
})
