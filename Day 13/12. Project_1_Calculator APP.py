# .............First project in python: calculator app................

# chapter 4: create function

def addition(num1, num2):
    result = num1+num2  # num1-value + num2-value =  result
    # .........we use .format() as we want to get the result in a style
    print("{0}+{1}={2}".format(num1, num2, result))


def subtraction(num1, num2):
    result = num1-num2  # num1-value + num2-value =  result
    print("{0}-{1}={2}".format(num1, num2, result))


def multiplication(num1, num2):
    result = num1*num2  # num1-value + num2-value =  result
    print("{0}*{1}={2}".format(num1, num2, result))


def division(num1, num2):
    if num2 == 0.0:
        # ...15/0 if one user give num2 = 0, then it shows the message
        print("cannot do divide by zero")
    else:
        result = num1/num2  # num1-value + num2-value =  result
        print("{0}/{1}={2}".format(num1, num2, result))

# Chapter 5 --- While Loop


while True:

    # chapter 1: display part

    print("What do you want to do?")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")
    print("Enter Q or q to exit the calculator")


# chapter 2: user input - 2 digit number

    choice = input("Enter your Choice:")  # it gives string value not integer
    if choice == 'Q' or choice == 'q':
        break  # ...it will help loop to stop
# taking a 2 number as a input from user

    # ...Here we use float to get the output in integer or float type not in string thats why we use type casting
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))

# chapter 3: condition port
    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        subtraction(num1, num2)
    elif choice == '3':
        multiplication(num1, num2)
    elif choice == '4':
        division(num1, num2)
    else:
        print("Invalid Choice")
