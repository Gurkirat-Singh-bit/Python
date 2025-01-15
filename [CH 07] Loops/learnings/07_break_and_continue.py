# here i learnt the use of break statement and continue statement 

l = [1,2,3,4,5,6,7,8,9]            # intialsing list for example to understand better 

for i in l:                        # intialsing for loop for list
 
    if i==4:                       # nested if used for conditon in loop

        break                      # break is used here to left the loop

    print(i)                       # this prints the list item

print("the program is done")       # this is used to verify whether program is done or not

t = (1,2,3,4,5,6,7,8,9)            # intialsing tuple for example to understand better 

for i in t:                        # intialsing for loop for tuple
 
    if i==4:                       # nested if used for conditon in loop

        continue                   # continue is used here to skip the iteration

    print(i)                       # this prints the list item

print("the program is done")       # this is used to verify whether program is done or not