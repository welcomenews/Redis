# file07-1.py

import os
import sys
import redis
import stat
from stat import *

def pipeline():
#path = 'C:/Windows/help'
  path = sys.argv[1]

  path_normalized = os.path.normpath(path)

  redis_client = redis.Redis(host = '127.0.0.1', port = 6379, decode_responses=True)

  pathp = "data:" + path_normalized + "*"
  pipeline = redis_client.pipeline()

  for key in redis_client.scan_iter(pathp):
    redis_client.delete(key)

  for dirpath, dirnames, filenames in os.walk(path_normalized):
      for file in filenames:  
        pathfile = "data:" + dirpath +"/"+ file
        keyRedis = dirpath +"/"+ file
        if os.path.isfile(keyRedis):
#          mode = ""
#          osStat = os.lstat(keyRedis)
#          mode = oct(osStat.st_mode)
#          print(mode[-3:])
          try:
            with open(keyRedis, 'r') as fp:
              temp = fp.read()
              pipeline.set(pathfile, temp)
#              print("Done!", '\n')
          except PermissionError:
              print("catch!")
  pipeline.execute()

pipeline()
