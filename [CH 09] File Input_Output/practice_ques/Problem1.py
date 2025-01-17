# Problem 1) Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poem.txt") as f :

    poem = f.read()
    
    if("twinkle" in poem):                                    # Check if the word 'twinkle' is in the poem

        print("this poem contains the word twinkle")          # If 'twinkle' is found, print a message
 
    else:

        print("this poem does not contain the word twinkle")  # If 'twinkle' is not found, print a different message

