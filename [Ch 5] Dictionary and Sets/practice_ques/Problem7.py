# Problem 7) If the names of 2 friends are same; what will happen to the program in problem 6?

# in that case, since this is dictionary key can't repeat so only one key stored but values can repeat


dictionary = {}

name = input("enter your name : ")                                                           
langauage = input("enter the name of the computer language you work with : ")
dictionary.update({name : langauage})

name = input("enter your name : ")                                              # taking names and language they work with
langauage = input("enter the name of the computer language you work with : ")   # after using update function, updating the 
dictionary.update({name : langauage})                                           # dictionary

name = input("enter your name : ")                                                           
langauage = input("enter the name of the computer language you work with : ")
dictionary.update({name : langauage})

name = input("enter your name : ")                                                           
langauage = input("enter the name of the computer language you work with : ")
dictionary.update({name : langauage})

print(dictionary)                                                               # verifying my answer by printing the dictionary