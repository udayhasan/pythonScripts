#!/usr/bin/python

n=raw_input("Enter number of terms you want to see: ")
n=int(n)
a=0
b=1
print (a)
print ("\t")
print (b)
print ("\t")

for i in range(2,n):
    c=a+b
    print (c)
    print ("\t")
    a=b
    b=c
