#.........Function in Python..........
#....Function is a group of statement that do a particular task in a few lines

#.........Syntax.....
''' 
  def function_name(parameter):
      #code to be executed
'''

#..........print hello world using function...................
#function declaration
#def hello_world():
    #function body
#    print("Hello World!")
#function calling
#hello_world() #...we can call the function as much as we can if we want to see the output more than once

#........function parameter/arguments..
#function declaration
#def hello_world(name): #here we declare name as a parameter of the function
    #function body
#    x = "Hello " + name
#    print(x)
#function calling
#hello_world("Hasib") #here we store Hasib as an argument of the parameter name

#.....program to print addition of two numbers using function....
def add_number(num1, num2):
    sum = num1 + num2
    print(sum)
    
add_number(10, 20) #always give the same number of arguments as variables while calling function otherwise program crash
    