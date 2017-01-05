import time
import random

list1 = [0, 1]
list2 = [0, 1]


score = 0
num1 = 0
num2 = 0
product = 0

print ("Welcome to the times table challenge")
name = input ("What is your first name?\n")
surname = input ("What is your last name?\n")
year = input("What year are you in?\n(please type a number)\n")
level = 1

if level == 1:
    for i in range (5):
        num1 = (random.choice(list1))
        num2 = (random.choice(list2))
        product = num1 * num2
        answer = input("What is " + str(num1) + " x " + str(num2) + "?\n")
        if answer == str(product):
            print ("correct")
            score = score+1
            print(score)
            if score == 3:
                level = level + 1
                print(level)
                if level == 2:
                    print("Next level")
                    list1.extend([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
                    list2.extend([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
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
    print ("You reached level " + str(level))



else:
    print ("I could not understand your entry")
