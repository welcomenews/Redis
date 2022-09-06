# pyton-redis-03.py
## при вызове вашей программы таким образом: .../pyton-redis-03.py lorem foo ipsum bar, если перед запуском значением ключа 
## lorem было 15, то в результате должно быть записано значение foo в ключ lorem-16-0, ipsum в ключ lorem-16-1 и bar в ключ 
## lorem-16-2. Ключ lorem должен по итогу хранить значение 16.

import redis
import sys

## redis_client = redis.Redis()
redis_client = redis.Redis(host = '127.0.0.1', port = 6379)

#def printValue(*ns):
def printValue():

  name = []
  id = 0
  i = 0

  for key in sys.argv:
    if (str(key) == '\0') | (str(key) == '0'):
      print("You can't transmit \\0")
      return()
     
    name.append(key)

  id = redis_client.incr(name[1])

  if len(name) != 1:
    
    res_args = id

    for key in name[2:]:
      redis_client.set(str(name[1]) +"-"+ str(res_args) +"-"+ str(i), str(key))
#      print(str(key) +"-"+ str(res_args) +"-"+ str(i))
      i+=1
          
    sys.exit(0)
          
printValue()

