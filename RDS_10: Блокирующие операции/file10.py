#  file10.py

import sys
import redis

def blocking():

  countN = int(sys.argv[1])
  keys = []

  for i in sys.argv[1:]:
    keys.append(i)

  redis_client = redis.Redis(host = '127.0.0.1', port = 6379, decode_responses=True)
   
  while True:
    for i in keys[1:]:
      temp = (redis_client.blmpop(5, 1, i, direction="left", count=countN))
      for i in temp[1][0:]:
        print(temp[0], i)
    sys.exit()    
  sys.exit('1')

blocking()
