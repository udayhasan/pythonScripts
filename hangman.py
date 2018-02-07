import random
import os

def wordSelect():
  f=open("dictionary.txt", "r")
  r=f.read()
  f.close()
  
  arr=r.split("\n")
  rand=arr[random.randint(0, len(arr))]
  return rand

def letterNumber(rand):
  arr=[]
  arr.extend(rand)
  num=len(arr)
  return arr, num

def inputTaker():
  c=raw_input("Please, give only one character at a time: ")
  return c.upper()

def inputValidate(c):
  arr=[]
  arr.extend(c)
  if(len(arr)>1):
    print "Invalid input, try again!"
    return 0
  else:
    return 1
    
def maker(c, arr, basic):
    
  for i in range (0, len(arr)):
    if (c==arr[i]):
      basic[i]=arr[i]

  return basic
  
def checker(rand, check):
  if(rand==check):
    return 1
  else:
    return 0

if __name__== "__main__":
  rand_main=wordSelect()
  [arr_main, num]=letterNumber(rand_main)
  
  win=0
  turn=0
  basic=[]
  for i in arr_main:
    basic.extend("*")
  
  first=""
  for i in basic:
    first=first+i
  print first
  
  while(win==0):
    
    print "you have "+str(len(arr_main)-turn)+" turn(s) left!"
    flag=0
    
    while(flag==0):
      c=inputTaker()
      os.system('clear')
      flag=inputValidate(c)
      
    basic=maker(c, arr_main, basic)
    check=""
    for i in basic:
      check=check+i
    print check
    
    checked=checker(rand_main,check)
    
    if(checked==1):
      win=1
    else:
      win=0
    
    turn=turn+1
    if(turn>=len(arr_main)):
        break
  
  if(win==1 and turn<=len(arr_main)):
    print "Game Over! You win!"
  else:
    print "Game Over! You Loose"
    
  
