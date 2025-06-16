#....................For Loop in Python................
''''
for variable in sequence:
    statement
'''
#......we use for loop in string, list and set type data

#looping through a list using for loop
my_friend = ["Mim", "Ebon", "Shuvo"]
#print(my_friend)
for friend in my_friend: #here for, in are keywords, friend is a new variable and my_friend is the sequence we want to acess
    #for loop body
    print(friend)

#Looping through a string 
my_name = "Hasib"
for name in my_name:
    print(name)
    
#the range() function

for x in range(5):  #indexing starts from 0 so that the output will be 0,1,2,3,4
    print(x)

#nested for loop

animal = ["Tiger", "Dog", "Cat"]
sound = ["roars", "barks", "meow"]

for x in animal:
    #body of x for loop
    for y in sound:
        #body of y nested for loop
        print("The " + x + " " + y)
