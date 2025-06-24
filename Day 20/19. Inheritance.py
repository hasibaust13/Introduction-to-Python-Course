#...............................Inheritance in Python....................
class Animal: #parent class of Dog class
    def __init__(self,name,age): #define a class
        self.name = name
        self.age = age
    def walk(self): #define a method under the class
        print(self.name + " walk")
##a.walk() #access the method 

class Dog(Animal): #child class
    def __init__(self,name,age): #we also pass the parameter of parent class Animal that is name
        super().__init__(name,age) #with super() we inherited the properties of method and parameters of parent class
    
    def sound(self):  #mathod of c child class
        print(self.name + " barks")
x = Dog("Tom", 1)
y = Dog("Jerry", 1)
x.walk()
x.sound()
y.walk()
y.sound()


