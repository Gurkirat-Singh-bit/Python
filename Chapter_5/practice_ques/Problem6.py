# Problem 6) Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

dictionary = {}                               # intialising an empty dictionary


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

print(dictionary)                                                               # printing the dictionary