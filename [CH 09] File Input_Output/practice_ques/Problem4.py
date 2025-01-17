# Problem 4) A file contains a word “Donkey” multiple times. 
# You need to write a program which replace this word with ##### by updating the same file. 


with open("file.txt") as f:                             # opening file in read mode

    content = f.read()                                  # reading file

    new_content = content.replace("Donkey", "#####")    # using replace, replacing donkey

with open("file.txt", "w") as f:                        # opening file in write
 
    f.write(new_content)                                # writing new content
    