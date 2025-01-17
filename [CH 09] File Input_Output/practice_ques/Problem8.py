# Problem 8) Write a program to make a copy of a text file “this. txt”

with open("poem.txt") as poem:             # opens an existing file 

    contents_p = poem.read()               # storing the contents of file

with open("this.txt", "w") as new:         # by using write mode to create as well as write a file

    new.write(contents_p)                  # copying the stores contents 
