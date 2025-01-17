# Problem 5) Repeat program 4 for a list of such words to be censored.

lst = ["ganda","donkey","gay"]                              # censored word add abusive word also ;)

with open("file.txt") as f:                             # opening file in read mode

    content = f.read()                                  # reading file

    for word in lst:

        content = content.replace(word, "#"* len(word))    # using replace, replacing censored words


with open("file.txt", "w") as f:                           # opening file in write mode            
 
    f.write(content)                                       # writing the contents