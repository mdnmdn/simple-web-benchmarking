from flask import Flask
from redis import Redis
from random import randint
from werkzeug.serving import run_simple

app = Flask(__name__)

redis = Redis("redis")

def randomKey():
  return "key_{}".format(randint(0,300))

@app.get('/')
def root():
  return 'ok - flask'

@app.get('/redis/incr')
def redis_incr():
  key = randomKey()
  val = redis.incr(key)
  return 'flask: {} - {}'.format(key, val)

if __name__ == '__main__':
  run_simple('localhost', 5000, app)
