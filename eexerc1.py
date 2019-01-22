# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:08:12 2019

@author: sort
"""

n = int(input())

if N<=100: 
        if N%2 !=0 :
            print("Weird")
        else:
            if (N% 2 ==0):
                if(N>=2 & N<=5):
                    print("Not Weird")
                elif (N>=6 & N<=20):
                    print("Weird")
                else:
                    if N>20:
                        print("Not Weird")
else:
    print("Enter Number between 1 and 100:")


    if n%2!=0: 
        print('Weird'); 
    elif n%2==0 and 2<=n<=5:
        print('Not Weird'); 
    elif n%2==0 and 6<=n<=20: 
        print('Weird'); 
    elif n%2==0 and n>20: 
        print('Not Weird');
        
        
2.Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

A = int(input())
B = int(input())

print(A+B)
print(A - B)
print(A*B)


3.Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .

You don't need to perform any rounding or formatting operations.


a = int(input())
b = int(input())

print(a//b)
print(a/b)

3.How to print squares of the numbers by getting input

n = int(input())


for i in range(n):
    print(i**2)
    
#for loop to print tables
    
n = int(input())

for i in range(1,12):
    print(n,'x',i,'=',n*i)


def is_leap(year):
    leap = False
    return bool year%4 ==0 and(year%400 ==0 or year%100!=0)

year = int(input())
print(is_leap(year))


The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year

#to print numbers for given n

n = int(input())
i = 1
for i in range(1,n+1):
    print i
    print(i,end='')#for printing the characters in a single line without space




