# .....................File in Python..............

# ....Creating a new file

# f = open("demo.txt", "x") #here 2 parameter are used in open() and both parameter will be ina quotation
# file operation (create)

# writing a file
# f = open("demo.txt", "w")
# f.write("I love python")

# append/ add new line in python
# f = open("demo.txt", "a")
# f.write(" and R")

# access the file we created

# f = open("demo.txt", "r")
# f.write("\n I love Javascript too")
# x = f.read()
# print(x)
# first_line = f.readline()
# print(first_line)
# f.close()

# delete a file

# import os # for deleting file, we have to import os
# os.remove("demo.txt")
# f = open("demo.txt", "r")
# f.close()

# ...Open an existing file

f = open(r"C:\Hasib\Research\Programming\Python\Blue Screen of Death (BDOS).txt", "r")
x1 = f.readline()
x2 = f.readline()
x3 = f.readline()
print(x1)
print(x2)
print(x3)
f.close()
