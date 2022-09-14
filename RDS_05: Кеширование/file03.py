# file03.py

#from file_read_backwards import FileReadBackwards
## Need pip install file-read-backwards

import os
import sys
import redis

def countBytes(): 

  fileAll = ""
  filename = sys.argv[1]

  redis_client = redis.Redis(host = '127.0.0.1', port = 6379, decode_responses=True)
  request = redis_client.get(filename)

  if(request):

    sys.stdout.write(request)

  else:
    with open(filename, 'r') as fp:
      while True:
        tmp100 = fp.read(100)
        if tmp100 == "":
            break
        
        if (sys.getsizeof(tmp100) > 130):
            fileAll = ""
        fileAll += tmp100

    byte100 = fileAll[-100:]
    redis_client.set(filename, byte100)

    sys.stdout.write(byte100)

countBytes()
