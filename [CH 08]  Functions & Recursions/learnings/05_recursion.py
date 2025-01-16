# here i learnt recursion in python

def factorial(num):                                      # function for factorial

    if(num==1 or num ==0):                               # base case
 
        return 1
    
    return num * factorial(num-1)                        # recursion i.e functions is calling itself
 

num = int(input("ENTER YOUR NUMBER :"))                  # taking input from the user 

print(f" THE FACTORIAL OF {num} IS {factorial(num)}")    # printing the factorial
