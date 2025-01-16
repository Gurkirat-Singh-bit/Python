# Problem 7) Write a python function to remove a given word from a list and strip it at the same time.

def rem(l, word):                                #  decleration of the function

    n =[]                                        # empty list for storing value

    for item in l:                               # loop from starting to the end of the list


        if not(item == word):                    # if item is not equal to word 

            n.append(item.strip(word))           # append stripped version of word

    return n                                     # return n a the last


l = ["shubham","rohan","an","anc","anshika"]     # list with some name

print(rem(l,"an"))                               # prinating the returned value recieved by calling function