#!/usr/bin/python
#This is a python code to count the number of emoticons in a file and display the percentage of occurance each emoticon

import re
import sys

def main():

  clines=0.0
  a=0.0
  b=0.0
  g=0.0
  c=0.0
  e=0.0
  d=0.0
  f=0.0
  cl=0.0
  a={}
  f= open('content.txt', 'rU')
  for line in f:
        cl=cl+1
  	a=0.0
  	b=0.0
  	c=0.0
  	d=0.0
  	e=0.0
  	f=0.0
 	match1 = re.findall(r'A.:',line)
 	for mat1 in match1:
	    clines=clines+1
	    match = re.findall(r':[)]', line)
	    for mat in match:
	      a=a+1
	      
	    match = re.findall(r':[(]', line)
	    #clines=clines+1exit()
	    for mat in match:
	      b=b+1
	      
	    match = re.findall(r';[)]', line)
	    #clines=#clines+1
	    for mat in match:
	      g=g+1
		    
	    match = re.findall(r':D', line)
	    #clines=#clines+1
	    for mat in match:
	      a=a+1
		  
	    match = re.findall(r':P', line)
	    #clines=#clines+1
	    for mat in match:
	      g=g+1
		    
	    match = re.findall(r'O[_]O', line)
	    #clines=#clines+1
	    for mat in match:
	      c=c+1
		    
	    match = re.findall(r':[-]o.', line)
	    #clines=#clines+1
	    for mat in match:
	      c=c+1
		 
	    match = re.findall(r':[-][/]', line)
	    #clines=#clines+1
	    for mat in match:
	      d=d+1
		    
	    match = re.findall(r'=[_]=', line)
	    #clines=#clines+1
	    for mat in match:
	      d=d+1
		
	    match = re.findall(r'B[-][)]', line)
	    #clines=#clines+1
	    for mat in match:
	      e=e+1
		    
	    match = re.findall(r'>[_]<', line)
	    #clines=#clines+1
	    for mat in match:
	      f=f+1
		    
	    match = re.findall(r'X[-][(]', line)
	    #clines=#clines+1
	    for mat in match:
	      f=f+1
  
  #a['1'] = (a/1) * 1
  #a['2'] = (b/1) * 1
  #a['3'] = (c/1) * 1
  #a['4'] = (d/1) * 1
  #a['5'] = (e/1) * 1
  #a['6'] = (f/1) * 1  
  print a 
  print clines
  print cl
  clines = 100
  p={}
  p['Happy'] = (a/clines) * 100
  #p['Sarca'] = (g/clines) * 100
  p['Neutral'] = (d/clines) * 100
  p['Surprised'] = (c/clines) * 100 
  p['Crook'] = (e/clines) * 100
  p['Angry'] = (f/clines) * 100
  p['Sad'] = (b/clines) * 100

  
  print '\nThe percentage of each mood is: \n'
  for k, v in p.items(): print k, ':', v 
 
 
if __name__ == '__main__':
     main()
 
