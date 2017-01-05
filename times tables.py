import time
import random

easy = [1, 2, 5, 10]
medium = [1, 2, 4, 5, 10, 11]
hard = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

score = 0
num1 = 0
num2 = 0
product = 0

print ("Welcome to the times table challenge")
name = input ("What is your first name?\n")
surname = input ("What is your last name?\n")
year = input("What year are you in?\n(please type a number)\n")
level = input("What level would you like?\n Easy   = 1\n Medium = 2\n Expert = 3\n\n")

if level == "1":
    for i in range (3):
        num1 = (random.choice(easy))
        num2 = random.randint(1,12)
        product = num1 * num2
        answer = input("What is " + str(num1) + " x " + str(num2) + "?\n")
        if answer == str(product):
            print ("correct")
            score = score+1
            print(score)
        else:
            print ("incorrect")
            #print (score)


    print ("\nWell done for completing the times tables challenge")
    time.sleep(1)
    print ("Your score was...")
    time.sleep(1)
    print ("...\n")
    time.sleep(1)
    print ("...\n")
    time.sleep(1)
    print ("...\n")
    time.sleep(1)
    print (str(score) + " points")

elif level == "2":
    for i in range (3):
        num1 = random.randint(0,12)
        num2 = random.randint(0,12)
        product = num1 * num2
        answer = input("What is " + str(num1) + " x " + str(num2) + "?\n")
        if answer == str(product):
            print ("correct")
            score = score+1
            print(score)
        else:
            print ("incorrect")
            print (score)


    print ("\nWell done for completing the times tables challenge")
    time.sleep(1)
    print ("Your score was...")
    time.sleep(1)
    print ("...\n")
    time.sleep(1)
    print ("...\n")
    time.sleep(1)
    print ("...\n")
    time.sleep(1)
    print (str(score) + " points")

elif level == "3":
    for i in range (3):
        num1 = random.randint(0,12)
        num2 = random.randint(0,12)
        product = num1 * num2
        answer = input("What is " + str(num1) + " x " + str(num2) + "?\n")
        if answer == str(product):
            print ("correct")
            score = score+1
            print(score)
        else:
            print ("incorrect")
            print (score)


    print ("\nWell done for completing the times tables challenge")
    time.sleep(1)
    print ("Your score was...")
    time.sleep(1)
    print ("...\n")
    time.sleep(1)
    print ("...\n")
    time.sleep(1)
    print ("...\n")
    time.sleep(1)
    print (str(score) + " points")

else:
    print ("I could not understand your entry")
