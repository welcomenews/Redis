# file07-2.py

import os
import sys
import redis

def pipeline():
#path = 'C:/Windows/help'
  path = sys.argv[1]

  path_normalized = os.path.normpath(path)

  redis_client = redis.Redis(host = '127.0.0.1', port = 6379, decode_responses=True)

  key = "data:" + "*"

  for i in redis_client.keys(key):
    size = redis_client.strlen(i)
    print(size, i[5:])

pipeline()
