#.................Dictionaries in Python.................
'''
dictionary_name = {
    key:value,  #...here key is a variable and value is the number we store in the variable
    key:value,
}


'''

#.......creating a dictionary
#person = {
#    "first_name":"Khan Md",  #here key is first name and value is Khan Md
#    "last_name": "Hasib",    #we divide the key and value with colon sign (:)
#    "age": 29
#}
#print(person)
#print(type(person)) #in dictionary the data type of the "dict"

#.......accessing item
#x = person["first_name"] #dictionary[key]
#y = person["last_name"]
#z = person["age"]
#print("First Name: ",x)
#print("First Name: ",y)
#print("First Name: ",z)

#.......get() method
#get_method = person.get("first_name")
#print(get_method)

#...........adding new items
#person["hobby"] = "Playing Cricket"
#print(person)

#.......changing item value
#person["first_name"] = "KHAN MD"
#print(person)

#......removing an item
#pop() method
#person.pop("last_name")
#print(person)
 
#..........nested dictionary
employee_data = {
    #nested dictionary
    "manager":{
        "name": "Hasib",   #we always seperate dictionary with comma in another dictionary
        "age": 29
        },
        "programmer":{
            "name": "Rahul",
            "age" : 32
        },
         "salary":{
             "manager_salary": 70000,
             "programmer_salary": 40000
         }
}

#....print manager name and age and salary
print("Manager name is: ", employee_data["manager"]["name"],
      "\nManager age is: ", employee_data["manager"]["age"],
      "\nManager salary is: ", employee_data["salary"]["manager_salary"], #...if we want to create new line, we can add \n in the program statement
      )

#....print programmer name and age and salary
print("Programmer name is: ", employee_data["programmer"]["name"],
      "\nProgrammer age is: ", employee_data["programmer"]["age"],
      "\nProgrammer salary is: ", employee_data["salary"]["programmer_salary"], #...if we want to create new line, we can add \n in the program statement
      )