#!/usr/bin/env python3

import os
import sys



def findFiles():
  bigFiles = {}
  list_files  = os.walk('/')
  for current_folder, subfolder, file_names in list_files:
    for file_name in file_names:
      absFilePath = os.path.join(current_folder,file_name)
      if os.path.exists(absFilePath) and os.path.getsize(absFilePath) > 104857600:
        bigFiles[absFilePath] = os.path.getsize(absFilePath)
  return bigFiles
  

def isRoot():
  #if os.getuid() != 0:
  #  return True
  #return False
  
  return (True if (os.getuid() != 0) else False)


if __name__ == '__main__':
  
  if isRoot():
    print("You NEED to be root in order to run this script !!!")
    sys.exit()
   
  bigFiles = findFiles()
  print(len(bigFiles))
  for file_name in bigFiles.keys():
    print(file_name,bigFiles[file_name])
  


