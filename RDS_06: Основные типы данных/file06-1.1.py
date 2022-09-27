# file06-1.1.py

import sys
import redis

def increaseList():

  filename = sys.argv[1]
 
  redis_client = redis.Redis(host = '127.0.0.1', port = 6379, decode_responses=True)

  user_input = input()
  request = user_input

  temp = request.split('\\n')

  for i in temp:

     redis_client.rpush(filename, i)
     redis_client.ltrim(filename, -20, -1)
  break

increaseList()
