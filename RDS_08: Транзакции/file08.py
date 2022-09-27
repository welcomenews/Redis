# file08.py

import os
import sys
import redis

def transaction():
   key = sys.argv[1]
   num = sys.argv[2]

   redis_client = redis.Redis(host = '127.0.0.1', port = 6379, decode_responses=True)

   count = 0 

   try:
     redis_client.watch(key)
     pipeline = redis_client.pipeline()

     count = int(redis_client.get(key))
     count += int(num)
     pipeline.set(key, count)
     pipeline.execute()
   except Exception:
    print("Catch!")

transaction()
