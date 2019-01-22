# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 12:51:22 2019

@author: sort
"""

#printing number pattern

from __future__ import print_function

num = int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print (j,end ="")
    print("\n")
       
        
#half pyramid
lastnum = 5
for i in range(1,lastnum+1):
    for j in range(1,i+1):
        print(j,end = "")
    print("\n")

#printing numbers rowise

n = int(input())

for i in range(1,n):
    for j in range(i,0,-1):   #range(start,stop,step)

        print(j,end = "")
    print("\n")
    

n = 10
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end = "")
    print("\n")
        
n = 5
for i in range(n,0,-1):
    print(i,end = " ")
print("\n")





n = 5

for i in range(n,0,-1):
    for j in range(1,i):
          print(j,end = "")
    print("\n")
    
n = int(input())

for i in range(-1+n,-1,-1):
    print(i,end = "")


#using format function in python

print("{},this is written in".format("python"))

str = "this is written in {}.{} is a good progm"
str.format("python","It")
#when there are multiple words to fill ,should specify it in the format fn

#using positional arguments for filling words

str =  "{0} is a {1} language"

str.format("python","It")


n = 10

for i in range(1,n+1):
    for j in range(-1+i,-1,-1):
        print(format(2**j,"5d"),end = "")
    print("\n")

#using function defintion to print pattern

def pattern(n):
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end = " ")
        print("\n")

n = int(input())

def wil_loop(n):
    while n in 5:
        n = n+1
        print(n)