import subprocess 

apis = {
  'node-express' : { 'url': 'http://localhost:9051' },
  'node-fastify' : { 'url': 'http://localhost:9052' },
  'python-flask' : { 'url': 'http://localhost:9053' },
  'python-fastapi' : { 'url': 'http://localhost:9054' },
  'go-bare-server' : { 'url': 'http://localhost:9055' },
}

test = {
  'empty-response' : { 'path': '/' },
  'redis-incr' : { 'path': '/redis/incr' },
}

def perform_test(url, concurrent_request = 10, duration_time = '3s'):
  cmd = 'siege -j -c {} -t {} {}'.format(concurrent_request, duration_time, url)
  proc = subprocess.run(cmd.split(' '), capture_output=True)
  print("cmd: ", cmd)
  print("proc: ", proc)
  return proc.stdout

def perform_test_on_all_apis(path):
  for api in apis:
    print(api)
    perform_test(apis[api]['url'] + path)

if __name__ == '__main__':
  url = apis['go-bare-server']['url'] + test['redis-incr']['path']
  perform_test_on_all_apis(test['redis-incr']['path'])
  #res = perform_test(url)