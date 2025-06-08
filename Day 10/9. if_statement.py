#................If_statment in Python...........
#x = 20
#y = 20

#if_statement
#if x<y:
    #body of if statement
 #   print("x is smaller than y")
#elif x>y:
    #body of elif
#    print("x is greater than y")
#elif x==y:
#    print("x and y are equal")
#else:
    #body of else part
#    print("enter right value") 

#.....program to find out the user is eligible for driving license or not
#user_age = int(input("Enter your age: "))

#if user_age>=18 and user_age<=45:
  #  print("you are eligible for driving license")
#elif user_age>=45 and user_age<=65:
#    print("your age is too high to chance to get driving license")
#else:
#    print("Sorry you are too young")
    
#....nested if statement
#x = 15
#if x>5:
#    print("x is more than 5")
    #nested if statement
 #   if x>10:
 #       print("x is less than 15")
 #   else:
 #       print("x is not more than 10")
        
        
x = 15
if x<2:
    print("x is more than 5")
    #nested if statement
    if x>10:
        print("x is less than 15")
    else:
        print("x is not more than 10")
else:
    print("The condition is false") #we write down the else statement as the first condition of if statement is false so that nested if statements are valueless