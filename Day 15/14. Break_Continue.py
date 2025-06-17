#.................Break and continue statement in python............
animal = ["tiger", "cat", "dog"]
for pet in animal:
    #print(pet)
    #if pet  == "cat":
      #break #stop the loop in a program (the output will be tiger, cat)
  
    #if pet  == "dog":
    #  break # but we want to see tiger as an output only, so we use break statement after the print statement
    #print(pet)
    
    if pet  == "cat":
      continue # stop the iteration of the loop for particular value but again run the iteration of the loop
    print(pet)
    