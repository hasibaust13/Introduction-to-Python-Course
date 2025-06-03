#.......Working with String

#..single/ double quotes
#..In python, make sure the quoattaion you used must be different; either single quotation or double quotation
#text = 'Hii I am Hasib, I love "Python" programming'
#print(text)

#..Multiline string

#text = '''I love Python, 
#it is a very easy programming language,
#the language is designed by Guido van Rossum'''
#print(text)

#...Concatenating String

#x = "Hello "
#y ="World!"
#z# = x+y
#p#rint(z)

#..Accessing parts of a string

#--indexing
#text ="I love Python"
#print(text)
#print the 1st character of the text: I
#print(text[0])
#print(text[5])

#slicing
#text ="Python lover"
#print(text[2:5]) #text[start index: ending index]

#..Capitalize String
name = "hasib"
x = name.capitalize()
print(x)
#-- convert to upper case
x = name.upper()
print(x)

#-- convert to lower case

x = name.lower()
print(x)

#-- get the lenght of a string
print(len(name))

#-- replacing parts of a string
text = "hello world!"
print(text)
y = text.replace("world", "hasib") #--- in replace function, we can use previous word first, then replace the new word with older one
print(y)