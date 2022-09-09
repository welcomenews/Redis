# file03.py

#from file_read_backwards import FileReadBackwards
## Need pip install file-read-backwards

import os
import sys

def countBytes(): 

  fileAll = ""

  with open(sys.argv[1], 'r', encoding='utf-8') as fp:
    while True:
      tmp100 = fp.read(100).replace('\n', "")
      if tmp100 == "":
          break
      
      if (sys.getsizeof(tmp100) > 99):
          fileAll = ""
      fileAll += tmp100

  byte100 = fileAll[-100:]

  print(byte100)
#  print(sys.getsizeof(byte100))
#  print(len(byte100.encode('utf-8')))

countBytes()
