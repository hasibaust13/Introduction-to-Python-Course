# ..............Project -2: Guess the number game in Python........

import random
# we want to take random numbers to make the game more enjoyable
mynumber = random.randint(0, 9)
# mynumber = 4 #computer guess number
print("I have a number in my mind, can you guess it?")
while True:  # we need while loop to continue the game in the program

    usernumber = int(input("Enter your guess: "))

    if usernumber == mynumber:
        print("Yes your guess is right")
        break  # AS we need to stop the game at certain point in the program
    elif usernumber > mynumber:
        print("The number you guess is greater than mynumber, \n Try again!")
    else:
        print("The number you guess is less than mynumber, \n Try again!")
