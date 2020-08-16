#!/usr/bin/env python3

import os
import sys
import argparse

def processFile():
  pass

if __name__ == '__main__':

 parser = argparse.ArgumentParser(description='A simple application for punching the clock')
 parser.add_argument('FILE',type=file,help="File to use")
 #parser.add_argument('-f','--file', type=str,help='File to record')
 args = parser.parse_args() 

 #with open(args.FILE,'r') as clock:
 #  for row in 
 
