# file09-1.py 

import random
import sys
import redis

def randomInt():

  name = sys.argv[1]
  defstr = "0000000000"
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  redis_client = redis.Redis(host = '127.0.0.1', port = 6379, decode_responses=True)

  while True:
    num = random.randint(0,999999999)
    deflist = list(defstr)
    for char in str(num):
      if char in numbers:
        tempint = int(deflist[int(char)])
        tempint += 1
        deflist[int(char)] = str(tempint)
    finalstring = ''.join(deflist)
    chanel = name + ":" + finalstring
    redis_client.publish(chanel, num)

randomInt()
