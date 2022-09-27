# file06-2.py

import sys
import redis

def increaseList(): 

  filename = sys.argv[1]
  limit = sys.argv[2]

  redis_client = redis.Redis(host = '127.0.0.1', port = 6379, decode_responses=True)
  
  records = redis_client.lpop(filename, limit)
  sys.stdout.write(str(records))

increaseList()
