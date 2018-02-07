import random

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
    
def show(c, arr):
  basic=[]
  for i in arr:
    if (c==i):
      basic.extend(c)
    else:
      basic.extend("*")
  return basic
  
def checker(rand, check):
  if(rand==check):
    return 1
  else:
    return 0
  
rand=wordSelect()
[arr, num]=letterNumber(rand)

win=0
turn=0

while(win==0 or trun <=len(arr)):
  basic=[]
  print "you have "+str(6-turn)+" turn(s) left!"
  flag=0
  while(flag==0):
    c=inputTaker()
    flag=inputValidate(c)
    
  basic=show(c,arr)
  check=""
  for i in basic:
    check=check+i
  checked=checker(rand,check)
  if(checked==1):
    win=1
  else:
    win=0
    
  turn +=1

if(win==1 and turn<=len(arr)):
  print "Game Over! You win!"
else:
  print "Game Over! You Loose"
  
  
