# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:34:43 2019

@author: sort
"""

#strings

# Silly Strings
# Demonstrates string concatenation and repetition
print("You can concatenate two " + "strings with the '+' operator.")
print("\nThis string " + "may not " + "seem terr" + "ibly impressive. " \
 + "But what " + "you don't know" + " is that\n" + "it's one real" \
 + "l" + "y" + " long string, created from the concatenation " \
 + "of " + "twenty-two\n" + "different strings, broken across " \
 + "six lines." + " Now are you" + " impressed? " + "Okay,\n" \
 + "this " + "one " + "long" + " string is now over!")
print("\nIf you really like a string, you can repeat it. For example,")
print("who doesn't like pie? That's right, nobody. But if you really")
print("like it, you should say it like you mean it:")
print("Pie" * 10)
input("\n\nPress the enter key to exit.")

#concatenating

print("you can concatenate two strings "+" with")

print("pie" * 10)


print("If a 2000 pound pregnant hippo gives birth to a 100 pound calf,")
print("but then eats 50 pounds of food, how much does she weigh?")
input("Press the enter key to find out.")
print("2000 - 100 + 50 =", 2000 - 100 + 50)

#operators maths

100+4

100-4

100/6

100//16

100*6


#greeting program
 name = "larry"
 
 print("Hi!",name)
 
 #getting input from users
 
 name = str(input("Hi what is your name"))
 
 print(name)
 
 print("Welcome",name)
 
 input("\n\n press enter to exit")
 
 
 #string manipulation
 
quote = "I think there is a world market for maybe five computers."
print("Original quote:")
print(quote)

print(quote.upper())

print(quote.lower())

print(quote.title())

print(quote.replace("five","100"))


print(
"""
 Trust Fund Buddy
Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).
Please enter the requested, monthly costs. Since you're rich, ignore
 pennies and use only dollar amounts.
"""
)
car = input("Lamborghini Tune-Ups: ")
rent = input("Manhattan Apartment: ")
jet = input("Private Jet Rental: ")
gifts = input("Gifts: ")
food = input("Dining Out: ")
staff = input("Staff (butlers, chef, driver, assistant): ")
guru = input("Personal Guru and Coach: ")
games = input("Computer Games: ")
total = car + rent + jet + gifts + food + staff + guru + games
print("\nGrand Total:", total)
input("\n\nPress the enter key to exit.")

#. {Write a program that allows a user to enter his or her two
#favorite foods. The program should then print out the name of
#a new food by joining the original food names together.}#


fav1 = raw_input("enter 1st favourite food:")
fav2 = raw_input("enter 2nd favourite food:")

print fav1 +  fav2

 #Write a Tipper program where the user enters a restaurant
#bill total. The program should then display two amounts: a
#15 percent tip and a 20 percent tip


name = int(input("enter bill total:"))

tip_15 = (name *15)/100

tip_20 = (name *20)/100

print tip_15,tip_20



#Write a Car Salesman program where the user enters the base
#price of a car. The program should add on a bunch of extra fees
#such as tax, license, dealer prep, and destination charge. Make
#tax and license a percent of the base price. The other fees
#should be set values. Display the actual price of the car once
#all the extras are applied.



base = int(input("Enter base price:"))

tax = (base * 20)/100

licens = (base * 10)/100

dealer = 5000

destin = 8000

actual = base - (tax+licens+dealer+destin)

print actual


#random number generation

import random
#random.choice
print ("A random number from list is : ",end="") 
print random.choice([1, 4, 8, 10, 3])

random.randrange(start,end,step)

print random.randrange(30,50,5)

#random numbers with a seed


random.seed(5) 
  
# printing mapped random number 
print ("The mapped random number with 5 is : ", end="")
print random.random()
  
# using seed() to seed different random number 
random.seed(7) 
  
# printing mapped random number 
print "The mapped random number with 7 is : ", end="" 
print random.random()

#random number

condtn  = random.choice([1,2,3])

if condtn == 1:
    print "Happy!"
 
if condtn == 2:
    print  "Neutral.."

if condtn == 3:
    print "Sad"


#three year old simulator

print("\tWelcome to the 'Three-Year-Old Simulator'\n")
print("This program simulates a conversation with a three-year-old child.")
print("Try to stop the madness.\n")
response = ""
while response != "Because.":
 response = input("Why?\n")
print("Oh. Okay.")
input("\n\nPress the enter key to exit.")


x, y = [int(x) for x in raw_input().split()]   

while x % 2 !=0:
    print "ok"

while y % 2 > 0:
    print "ok"


#treating a value as a condition

# Maitre D'
# Demonstrates treating a value as a condition
print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening.\n")
money = int(input("How many dollars do you slip the Maitre D'? "))
if money:
 print("Ah, I am reminded of a table. Right this way.")
else:
 print("Please, sit. It may be a while.")
input("\n\nPress the enter key to exit.")
 
#Testing another condition
 
 
marks = int(input("How much marks you got?"))
 
if marks :
     print("You are free")
else:
    print("Taje class")


count = 0
while True:
 count += 1
 # end loop if count greater than 10
if count > 10:
    break
 # skip 5
if count == 5:
    continue
print(count)
input("\n\nPress the enter key to exit.")



