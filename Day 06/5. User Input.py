#....user input

#name = input("Enter your name: ")
#print(name)
#print("Welcome Mr:", name)

#num1 = input("Enter Number one:")
#num2 = input("Enter Number two:")
#result = num1 + num2
#print(result)
#--- here the results come in string format as input function always give string format output

#---when you convert the data type, we can use datatype() str() float() bool()
num1 = input("Enter Number one:")
num2 = input("Enter Number two:")
result = int(num1) + int(num2)
print(result)