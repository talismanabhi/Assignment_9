#!/usr/bin/python
#This is a python code to count the number of emoticons in a file and display the percentage of occurance each emoticon

import re
import sys

def main():

  clines=0
  chappy=0
  csad=0
  csarca=0
  csurp=0
  ccrook=0
  cneutral=0
  cangry=0
  f= open('content.txt', 'rU')
  for line in f:
    match = re.findall(r':[)]', line)
    clines=clines+1
    for mat in match:
      chappy=chappy+1
  
  if clines:    
    print clines
  else:
    print 'None'
    
  if chappy:    
    print chappy
  else:
    print 'None happy'
    
  print 'working'
    #print chappy
    
 
if __name__ == '__main__':
     main()
 
