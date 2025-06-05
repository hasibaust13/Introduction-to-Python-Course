#......Lists in Python
#--List is a ordered container

#--create a list
#pets = [] # this is called empty list

#pets = ["Dog", "Cat", "Horse", "Camel"] #In list, the value we entered called element #0,1,2
        #0   ,   1  ,     2  ,   3 -- positive indexing
        #-4  ,  -3,       -2,   -1 -- negative indexing
#print(pets)

#---print only the first element of the list
#Indexing
#print(pets[0]) #access the 1st element
#print(pets[3]) #access the last element

#Negative Indexing
#print(pets[-3])
#print(pets[-2])

#--Range of Indexes
#print(pets[1:3]) #--  here we get the output of Cat, Horse as they are in between 1st element and last element

#--Adding items to a list
#pets.append("Elephant") #append()
#print(pets)

#pets.insert(0, "Kangaroo") #insert() --- insert(index number, item name)
#print(pets)

#...Deleting items from a list

#pets.pop() #always delete the last element from the list 
#print(pets)
#pets.remove("Cat") #if we want to delete specific item from the list, we use use remove()
#print(pets)

#...getting the length of a list
#print(len(pets))

#...Changing the item value
#pets[1] = "Cow"
#print(pets)

#pets[3] = "Monkey"
#print(pets)

#---Extending a list
#num1 = [1,2,3]
#num2 = [4,5,6]
#num1.extend(num2) #....we can extend() to extending a list of numbers serially
#print(num1)

#---Check if an item exists
#membership operator - in/ not in

#country = ["Bangladesh", "Australia", "USA", "England"]
#check_item = "Australia" in country 
#check_item = "Newzeland" in country
#print(check_item) # if the item is involved in the list, it shows true otherwise false
country = ["Bangladesh", 2, 2.5, True]
#check_item = "Newzeland" not in country
#print(check_item)
print(country) #........... we can store any type of data in list and get the output