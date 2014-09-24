#!/usr/bin/python
#This is a python code to count the number of emoticons in a file and display the percentage of occurance each emoticon

import re
import sys

def main():

  clines=0.0
  chappy=0.0
  csad=0.0
  csarca=0.0
  csurp=0.0
  ccrook=0.0
  cneutral=0.0
  cangry=0.0
  f= open('content.txt', 'rU')
  for line in f:
    match = re.findall(r':[)]', line)
    clines=clines+1
    for mat in match:
      chappy=chappy+1
         
    match = re.findall(r':[(]', line)
    #clines=clines+1
    for mat in match:
      csad=csad+1
      
    match = re.findall(r';[)]', line)
    #clines=#clines+1
    for mat in match:
      csarca=csarca+1
               
    match = re.findall(r':D', line)
    #clines=#clines+1
    for mat in match:
      chappy=chappy+1
             
    match = re.findall(r':P', line)
    #clines=#clines+1
    for mat in match:
      csarca=csarca+1
               
    match = re.findall(r'O[_]O', line)
    #clines=#clines+1
    for mat in match:
      csurp=csurp+1
               
    match = re.findall(r':[-]o.', line)
    #clines=#clines+1
    for mat in match:
      csurp=csurp+1
              
    match = re.findall(r':[-][/]', line)
    #clines=#clines+1
    for mat in match:
      cneutral=cneutral+1
               
    match = re.findall(r'=[_]=', line)
    #clines=#clines+1
    for mat in match:
      cneutral=cneutral+1
           
    match = re.findall(r'B[-][)]', line)
    #clines=#clines+1
    for mat in match:
      ccrook=ccrook+1
               
    match = re.findall(r'>[_]<', line)
    #clines=#clines+1
    for mat in match:
      cangry=cangry+1
               
    match = re.findall(r'X[-][(]', line)
    #clines=#clines+1
    for mat in match:
      cangry=cangry+1
      
  p={}
  p['Happy'] = (chappy/clines) * 100
  p['Sarca'] = (csarca/clines) * 100
  p['Neutral'] = (cneutral/clines) * 100
  p['Surprised'] = (csurp/clines) * 100 
  p['Crook'] = (ccrook/clines) * 100
  p['Angry'] = (cangry/clines) * 100
  p['Sad'] = (csad/clines) * 100

  
  print '\nThe percentage of each mood is: \n'
  for k, v in p.items(): print k, ':', v, '%'
 
 
if __name__ == '__main__':
     main()
 
