# Problem 5) Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def pattern(n):                               # recursive functions for printing patterm

    if(n==0):                                 # base case for recursive function
 
        return                               
        
    print("*"* n)                             # printings the patter

    pattern(n-1)                              # recursive call to function again

num = int(input("ENTER ANY NUMBER : "))       # taking n from the user
 
pattern(num)                                  # calling the function
  