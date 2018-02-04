import random
import os

start=0 
end=100

win=0

while (win==0):
  guess=random.randint(start,end)
  print guess
  
  flag=raw_input("match/high/low: ")
  
  if (flag=="match"):
    win=1
  elif(flag=="high"):
    end=guess
  else:
    start=guess
  os.system('clear')
  
print "You Win! Game Over!"
