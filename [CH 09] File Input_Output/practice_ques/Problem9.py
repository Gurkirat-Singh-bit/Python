# Problem 9) Write a program to find out whether a file is identical & matches the content of another file.



with open("poem.txt") as poem:                               # opens an existing file 

    contents_poem = poem.read()                              # storing the contents of file



with open("this.txt") as this:                               # opens an existing file 

    contents_this = this.read()                              # storing the contents of file


if contents_poem == contents_this:                           # check if contents of both file are same 

    print("the file contains same contents")                 # print that they are same

elif contents_poem != contents_this:                         # check if contents of both file are different

    print("the file does not contains same contents")        # print that they are different

else:                                                        # if both are false something went wrong
 
    print("Something went wrong")                            # printing something went wrong