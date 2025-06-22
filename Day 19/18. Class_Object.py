# ...............Class % Object in Python...........

# class python

# class person:
# body of person class
# class properties
#    first_name = "Hasib"
#    last_name = "Khan"
#    age = 29

# person_obj = person() #class object
# access properties
# firstname = person_obj.first_name
# lastname = person_obj.last_name
# age = person_obj.age
# print the value of person class
# print("First Name: ",firstname)
# print("Last Name: ",lastname)
# print("Age: ",age)

# class with attribute
# creating an instance of the class
# class student:
#    def __init__(self,id_number,name,age): #here we define init function where tow parameter: self, multiple factors of class
#        self.id_number = id_number #self parameter helps to get the access of other parameters in the init function
#        self.name = name
#        self.age = age

# student_obj = student(2727, "Hasib", 29) #instance - object created from the class
# x = student_obj.id_number
# y = student_obj.name
# z = student_obj.age

# print("Student Roll No is:", x)
# print("Student Name is:", y)
# print("Student age is:", z)

# instance are always unique

# Methods in python
class student:
    def __init__(self, id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age

    def great_student(self):  # we can define methods under the class with self parameter
        print("Hello " + self.name + " How are you?")


student_obj = student(2727, "Hasib", 29)
student_obj.great_student()  # we can access the method here
x = student_obj.id_number
y = student_obj.name
z = student_obj.age

print("Student Roll No is:", x)
print("Student Name is:", y)
print("Student age is:", z)
