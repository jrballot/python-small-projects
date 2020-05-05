#!/usr/bin/env python3

import os
import sys
import argparse

def findFiles(path,sizeOver=1):
  bigFiles = {}
  list_files  = os.walk(path)
  for current_folder, subfolder, file_names in list_files:
    if current_folder.startswith('/proc') or current_folder.startswith('/dev'):
      continue
    for file_name in file_names:
      absFilePath = os.path.join(current_folder,file_name)
      if os.path.exists(absFilePath) and os.path.getsize(absFilePath) >= sizeOver:
        bigFiles[absFilePath] = os.path.getsize(absFilePath)
  return bigFiles
  

def isRoot():
  return (True if (os.getuid() == 0) else False)


if __name__ == '__main__':
  
  if not isRoot():
    print("You NEED to be root in order to run this script !!!")
    sys.exit()
  
  parser = argparse.ArgumentParser(description="Find big files on you running system")
  parser.add_argument('PATH', type=str ,help='Base path to check files size.')
  parser.add_argument('-t','--top', type=int ,help='Return the TOP N biggest files.')
  parser.add_argument('-so','--sizeover', type=str ,help="Only return files over specified size. For example: 1M, 10M, 100M, 1G, 10G, 100G.")
  args = parser.parse_args()
  magnitude = {'M':1048576,'G':1073741824}
  sizeOver = 1  

  if args.sizeover != None:
    sizeOver = int(args.sizeover[:int(len(args.sizeover)-1)])
    sizeOverMagnitude = args.sizeover[-1:]
    sizeOver = sizeOver * magnitude[sizeOverMagnitude]
  else:
    print('Size not specifies in nM or nG. For example: 1M, 10M, 100M, 1G, 10G, 100G')
    sys.exit()
    
  bigFiles = findFiles(args.PATH,sizeOver)
  sortedBigFiles = sorted(bigFiles.items(), key=lambda x: x[1], reverse=True)

  if args.top != None:
    for file_name,file_size in sortedBigFiles[:args.top]:
      print("{} {}{}".format(file_name,file_size//magnitude[sizeOverMagnitude],sizeOverMagnitude))
    sys.exit()

  for file_name,file_size in sortedBigFiles:
    print("{} {}{}".format(file_name,file_size//magnitude[sizeOverMagnitude],sizeOverMagnitude))
  sys.exit()

