# here i learnt with satatement in python

# f = open("file.txt")                # opening a file.txt

# print(f.read())                     # reading as well as printing the file.txt
 
# f.close()                           # closing the file

# the same can be done using with statement
# like this

with open("file.txt") as f :          # this is used here for opening file.txt as f

    print(f.read())                   # this is for printing its content

# and in with we dont have to explicitly close the file