# here i learnt how to write a file in python

st = "hi my namer is gurkirat"              # string that is to be write in file

f = open("myfile.txt", "w")                 # this will open a file in write mode as well as create it

f.write(st)                                 # this will write the string in file

f.close                                     # closing the file