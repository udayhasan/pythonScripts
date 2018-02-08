import json
import os
from bokeh.plotting import figure, show, output_file

def add():
    dictionary={}
    with open("birthday.json", "r") as f:
        dictionary=json.load(f)
    
    addName=raw_input("Enter name: ")
    addDate=raw_input("Enter Birthday: ")
    dictionary[addName]=addDate
    
    with open("birthday.json", "w") as f:
        json.dump(dictionary, f)
    
    print('Info for {} is added!' .format(addName))

def find ():
    dictionary={}
    with open("birthday.json", "r") as f:
        dictionary=json.load(f)
    
    name=raw_input("Who's birthday you want to check?\n")
    
    try :
        if dictionary[name]:
            print('{} is born on {}\n'.format(name, dictionary[name]))
    except KeyError:
        print('{} is not in the list\n'.format(name))
        
def available():
    dictionary={}
    with open("birthday.json", "r") as f:
        dictionary=json.load(f)
    
    for i in dictionary.keys():
        print i

def byMonth():
    monthName=[]
    month=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    monthWise={}
    months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    for i in months:
        monthWise[i]=0
    
    dictionary={}
    with open("birthday.json", "r") as f:
        dictionary=json.load(f)
    
    for i in dictionary.keys():
        s=dictionary[i].split("/")
        name=int(s[0].encode('utf-8'))
        if name not in monthName:
            monthName.append(name)
    
    for j in monthName:
        for i in dictionary.keys():
            s2=dictionary[i].split("/")
            num=int(s2[0].encode('utf-8'))
            if (j==num):
                month[j-1]+=1
                
    for i in range (0, len(month)):
        if(i==0):
            monthWise['January']=month[i]
        elif(i==1):
            monthWise['February']=month[i]
        elif(i==2):
            monthWise['March']=month[i]
        elif(i==3):
            monthWise['April']=month[i]
        elif(i==4):
            monthWise['May']=month[i]
        elif(i==5):
            monthWise['June']=month[i]
        elif(i==6):
            monthWise['July']=month[i]
        elif(i==7):
            monthWise['August']=month[i]
        elif(i==8):
            monthWise['September']=month[i]
        elif(i==9):
            monthWise['October']=month[i]
        elif(i==10):
            monthWise['November']=month[i]
        else:
            monthWise['December']=month[i]
          
    for i in months:
        if (monthWise[i]!=0):
            print i, "\t:\t", monthWise[i]

def plotter():
    output_file("plot.html")
    x=[]
    y=[]
    
    monthName=[]
    month=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    monthWise={}
    months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    for i in months:
        monthWise[i]=0
    
    dictionary={}
    with open("birthday.json", "r") as f:
        dictionary=json.load(f)
    
    for i in dictionary.keys():
        s=dictionary[i].split("/")
        name=int(s[0].encode('utf-8'))
        if name not in monthName:
            monthName.append(name)
    
    for j in monthName:
        for i in dictionary.keys():
            s2=dictionary[i].split("/")
            num=int(s2[0].encode('utf-8'))
            if (j==num):
                month[j-1]+=1
                
    for i in range (0, len(month)):
        if(i==0):
            monthWise['January']=month[i]
        elif(i==1):
            monthWise['February']=month[i]
        elif(i==2):
            monthWise['March']=month[i]
        elif(i==3):
            monthWise['April']=month[i]
        elif(i==4):
            monthWise['May']=month[i]
        elif(i==5):
            monthWise['June']=month[i]
        elif(i==6):
            monthWise['July']=month[i]
        elif(i==7):
            monthWise['August']=month[i]
        elif(i==8):
            monthWise['September']=month[i]
        elif(i==9):
            monthWise['October']=month[i]
        elif(i==10):
            monthWise['November']=month[i]
        else:
            monthWise['December']=month[i]

    for i in months:
        x.append(i)
        y.append(monthWise[i])
        
    p = figure()
    p.vbar(x=x, top=y, width=0.5)
    show(p)
    
if __name__=="__main__":
    while (True):
        select=input("1. Available\n2. Add\n3. Find\n4. By Month\n5. Plot By Month\n6. Quit\n\n")
        if(select==1):
            os.system('clear')
            available()
        elif(select==2):
            os.system('clear')
            add()
        elif(select==3):
            os.system('clear')
            available()
            find()
        elif(select==4):
            os.system('clear')
            byMonth()
        elif(select==5):
            os.system('clear')
            plotter()
        elif(select==6):
            os.system('clear')
            print "Program Ended!"
            break
        else:
            print "Invalid input! Try again!"
    
