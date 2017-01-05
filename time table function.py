import time
import random

list1 = [0, 1]
list2 = [0, 1]


score = 0
num1 = 0
num2 = 0
product = 0
level = 1

def bler():
    print ('Bler')

def times():
    num1 = (random.choice(list1))
    num2 = (random.choice(list2))
    product = num1 * num2
    answer = input("What is " + str(num1) + " x " + str(num2) + "?\n")
    if answer == str(product):
        print ("\nCorrect\n")
        global score
        score = score+1
        if score > 1:
            global level
            level= level+1
            # write to file at this point clarify column based on level

def divide():
    num1 = (random.choice(list1))
    num2 = (random.choice(list2))
    product = num1 * num2
    answer = input("What is " + str(product) + " / " + str(num1) + "?\n")
    if answer == str(num2):
        print ("\nCorrect\n")
        global score
        score = score+1
        


print ("Welcome to the times table challenge")
name = input ("What is your first name?\n")
surname = input ("What is your last name?\n")
year = input("What year are you in?\n(please type a number)\n")
# Check whether file exists at this point
# Create file csv? at this point (Date reference)
# Add the name, year etc at this point to file

if level == 1:
    print ("Level - " + str(level) + "\n")
    score = 0
    for i in range(2):
        times()

if level == 2:
    print ("Level - " + str(level) + "\n")
    score = 0
    list1 = [3, 3]
    list2 = [3, 3]
    for i in range(2):
        times()

if level == 3:
    print ("Level - " + str(level) + "\n")
    score = 0
    list1 = [7]
    list2 = [7]
    for i in range(2):
        times()
        divide()
        times()


print ("Congratulations on completing the times table challenge\n")
print ("You reached level...\n\n")
print (str(level))
