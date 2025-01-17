# here i learnt how to append in the file

st = "\n this is a file"

f = open("file.txt", "a")                # this will open this file in append mode

f.write(st)                              # this will add this file line in file.txt

f.close()                                # close the file