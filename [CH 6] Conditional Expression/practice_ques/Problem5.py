# Problem 5) Write a program which finds out whether a given name is present in a list or not.

name_list = ["gurkirat","harshit","gaurav","vansh"]          # intialising a list with some names

name = input("ENTER NAME YOU WANT TO SEARCH : ")              # taking the name from the user

if(name in name_list):                                        # if list contain name then its prints it contains
    print("THE NAME IS PRESENT IN THE LIST") 

else:
    print("LIST DOES'NT CONTAINS THIS NAME")                  # else this is not in the list 