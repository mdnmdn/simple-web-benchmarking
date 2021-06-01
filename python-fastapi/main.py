from random import randint
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from asyncio_redis import Connection, Pool

app = FastAPI()

connection = None

def randomKey():
  return "key_{}".format(randint(0,300))

@app.on_event("startup")
async def startup():
  global connection
  connection = await Connection.create(host="redis")
  # connection = await Pool.create(host="redis")

@app.get("/", response_class=PlainTextResponse)
def read_root():
  return 'ok - fastapi'

@app.get("/redis/incr", response_class=PlainTextResponse)
async def redis_incr():
  key = randomKey()
  val = await connection.incr(key)
  return 'fastapi: {} - {}'.format(key, val)