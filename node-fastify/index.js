const fastify = require('fastify')()

const port = process.env.PORT || 3000
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


fastify.get('/', async (req, res) => {
  return 'ok - fastify';
});

fastify.listen(port, '0.0.0.0', err => {
  if (err) throw err
  console.log(`server listening on ${fastify.server.address().port}`)
})
