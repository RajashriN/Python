# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:33:03 2019

@author: sort
"""
import random

#pick a random number
#while the player hasn’t guessed the number
 #let the player guess
#congratulate the player

print("Welcome to guess my number game")
tries = random.randint(1,100)


guess = 1


num  = int(input("enter number"))

while tries!=num:
    if (tries > num):
        print("Bit lower")
        guess = int(input("another"))
    elif (tries < num):
        print("Bit Higher")
        guess = int(input("another"))
    else: 
        print("Congrats you are right")
        print("Press / to exit")
        