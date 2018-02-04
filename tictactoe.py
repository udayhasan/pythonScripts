import os
basic= [["*", "*", "*"],
        ["*", "*", "*"],
        ["*", "*", "*"]]

turn=0
win=0

c1="O"
c2="X"

def inputValidate(x,y):
  if(x>2 or x<0 or y>2 or y<0):
    print "Invalid input, try again!"
    return 0
  elif(basic[x][y]!="*"):
    print "Invalid input, try again!"
    return 0
  else:
    return 1

def inputTaker():
  x=input("input x co-ordinate: ")
  y=input("input y co-ordinate: ")
  return x,y

def boardMaker(checked):
  dim=3

  for i in  range (0, dim):
    dash=" "
    bar=""
    for j in  range (0, dim):
      dash=dash+"---"
      dash=dash+" "
      bar=bar+"|"
      bar=bar+" "
      bar=bar+str(checked[i][j])
      bar=bar+" "
    bar=bar+"|"
    print dash
    print bar
  
  
  dash=" "
  for i in  range (0, dim):
    dash=dash+"---"
    dash=dash+" "
  print dash

def check (checked):
  winner=0
  
  if   (checked[0][0]==checked[0][1] and checked[0][1]==checked[0][2] and checked[0][0]!="*"):
    winner=1
  elif (checked[1][0]==checked[1][1] and checked[1][1]==checked[1][2] and checked[1][0]!="*"):
    winner=1
  elif (checked[2][0]==checked[2][1] and checked[2][1]==checked[2][2] and checked[2][0]!="*"):
    winner=1
  elif (checked[0][0]==checked[1][0] and checked[1][0]==checked[2][0] and checked[0][0]!="*"):
    winner=1
  elif (checked[0][1]==checked[1][1] and checked[1][1]==checked[2][1] and checked[0][1]!="*"):
    winner=1
  elif (checked[0][2]==checked[1][2] and checked[1][2]==checked[2][2] and checked[0][2]!="*"):
    winner=1
  elif (checked[0][0]==checked[1][1] and checked[1][1]==checked[2][2] and checked[0][0]!="*"):
    winner=1
  elif (checked[2][0]==checked[1][1] and checked[1][1]==checked[0][2] and checked[2][0]!="*"):
    winner=1
    
  return winner

boardMaker(basic)

while (turn<9 and win ==0):
  if(turn%2==0):
    print "Player-1:"
    valid=0
    while (valid!=1):
      [x,y]=inputTaker()
      valid=inputValidate(x,y)
    basic[x][y]=c1
    os.system('clear')
    boardMaker(basic)
    if(check(basic)):
      print "Player 1 Wins!"
      break
    
  else:
    print "Player-2:"
    valid=0
    while (valid!=1):
      [x,y]=inputTaker()
      valid=inputValidate(x,y)
    basic[x][y]=c2
    os.system('clear')
    boardMaker(basic)
    if(check(basic)):
      print "Player 1 Wins!"
      break

  turn+=1

print "Game Over"
