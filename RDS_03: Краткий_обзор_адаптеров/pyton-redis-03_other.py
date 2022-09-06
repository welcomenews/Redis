## pyton-redis-03.py
## при вызове вашей программы таким образом: .../pyton-redis-03.py, если перед запуском значением ключа lorem было 15,
## то в результате должно быть записано значение переданные в аргументах cool в ключ cool-1-0, ret в ключ ret-1-1. 
## Ключ lorem должен по итогу хранить значение 16.

import redis
import sys

## redis_client = redis.Redis()
redis_client = redis.Redis(host = '127.0.0.1', port = 6379)

def printValue(*ns):

  name = []
  id = 0
  i = 0

  for key in ns:
    if (key == '\0') | (key == 0):
      print("You can't transmit \\0")
      return()

    name.append(key)

  id = redis_client.incr(name[0])

  if len(name) != 1:
    
    res_args = id

    for key in name[1:]:
      redis_client.set(str(key) +"-"+ str(res_args) +"-"+ str(i), str(key))
#      print(str(key) +"-"+ str(res_args) +"-"+ str(i))
      i+=1
          

printValue("foo", "cool", 'ret')

