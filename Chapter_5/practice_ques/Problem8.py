# Problem 8) If languages of two friends are same; what will happen to the program in problem 6?

# in that case, since this is dictionary key can't repeat but values can repeat so different friends can have same language

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