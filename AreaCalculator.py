"""
This program does the area calculate
wang
"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
print "Now this program is running"

print "Current time: %s/%s/%s %s:%s"%(now.month,now.day,now.year,now.hour,now.minute)

sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == 'C':
  radius = raw_input("Input the radius: ")
  radius = float(radius)
  area = pi * radius ** 2
  print "The pie is baking..."
  sleep(1)
  print ("Area: %.2f.\n%s" %(area,hint) )
elif option == 'T':
  base = float(raw_input("Enter the base: "))
  height = float(raw_input("Enter the height: "))
  area = base * height * (0.5)
  print "Uni Bi Tri..."
  sleep(1)
  print ("Area: %.2f.\n%s" %(area,hint) )
else:
  print "I'm so sorry that you have entered the garbage. \nThe program is exiting..."
  
  
