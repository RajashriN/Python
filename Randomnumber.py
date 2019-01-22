# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 18:10:51 2019

@author: sort
"""

# Craps Roller
# Demonstrates random number generation
import random
# generate random numbers 1 - 6
die1 = random.randint(1, 1000)
die2 = random.randrange(1000) + 1
total = die1 + die2
print("You rolled a", die1, "and a", die2, "for a total of", total)
input("\n\nPress the enter key to exit.")


import random

print("I sense your energy. Your true emotions are coming across my screen.")
print("You are...")
mood = random.randint(1, 3)
if mood == 1:
 # happy
 print( \
 """
 -----------
 | |
 | O O |
 | < |
 | |
 | . . |
 | `...` |
 -----------
 """)
elif mood == 2:
 # neutral
 print( \
 """
 -----------
 | |
 | O O |
 | < |
 | |
 | ------ |
 | |
 -----------
 """)
elif mood == 3:
 # sad
 print( \
 """
 -----------
 | |
 | O O |
 | < |
 | |
 | .'. |
 | ' ' |
 -----------
 """)
else:
 print("Illegal mood value! (You must be in a really bad mood).")
print("...today.")
input("\n\nPress the enter key to exit.")
