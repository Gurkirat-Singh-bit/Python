# Problem 4) Write a recursive function to calculate the sum of first n natural numbers.

def sum(num):                           # RECURSIVE FUNCTION FOR SUM OF NATURAL NUMBER

    if(num==0):                         # base case 

        return 0
    
    if(num==1):

        return 1                        # base case 
    
    return sum(num-1) + num             # recursive part of the function


num = int(input("ENTER NUMBER TILL YOU WANT SUM OF NATURAL NUMBER : "))

# taking number from the user 

print(F"THE SUM OF 1 TO {num} IS {sum(num)}") # printing the sum