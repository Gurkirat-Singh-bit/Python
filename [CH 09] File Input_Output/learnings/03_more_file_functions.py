# here i learnt more file i/o functions in python

f = open("file.txt")                     # this will open this file in read mode

# lines = f.readlines()                    # this will read all the lines of file and store them in a list

# print(lines, type(lines))                # this will print the list of lines and its type

# line1 = f.readline()                     # this will read the file line by line

# print(line1, type(line1))                # this will print the line and its type

# line2 = f.readline()                     # this will read the file line by line

# print(line2, type(line2))                # this will print the line and its type

line = f.readline()                       # this will read the file line by line

while(line != ""):
    print(line)
    line = f.readline()

f.close()                                # this will close the file