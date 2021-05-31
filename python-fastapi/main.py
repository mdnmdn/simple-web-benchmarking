from random import randint
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from asyncio_redis import Connection

app = FastAPI()

connection = None

def randomKey():
  return "key_{}".format(randint(0,300))

@app.get("/", response_class=PlainTextResponse)
def read_root():
    return 'ok - fastapi'

@app.get("/redis/incr", response_class=PlainTextResponse)
async def redis_incr():
  global connection
  if connection == None:
    connection = await Connection.create(host="redis")

  key = randomKey()
  val = await connection.incr(key)
  return 'fastapi: {} - {}'.format(key, val)