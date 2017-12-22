#!/usr/bin/python
a=[1, 13, 20, 1, 10, 7, 9, 0, 3, 2, 1, 2]
n=len(a)

for i in range(0, n-1):
    for j in range(0, n-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            
for k in range(0, n):
    print(a[k])
