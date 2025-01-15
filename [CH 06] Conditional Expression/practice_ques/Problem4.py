# Problem 4) Write a program to find whether a given username contains less than 10 characters or not.

Username = input("ENTER USERNAME YOU WANT : ")                  # taking user name from the user

if(len(Username)>10):                                           # checking whether the length of name is greater than 10
    print("PLEASE ENTER USER NAME UNDER 10 CHARACTERS")

else: 
    print("THIS USERNAME WORKS")                                # if ,"if" condition not happens then it executes