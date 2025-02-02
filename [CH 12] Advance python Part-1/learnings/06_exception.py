# here i learning exception handling in python

# There are many built-in exceptions which are raised in python when something goes 
# wrong.
# Exception in python can be handled using a try statement. The code that handles the 
# exception is written in the except clause.


try:                                                  # try check whether things works or not

    print(num :=  int(input("Enter a number :")))


except Exception as e:                                 # if not dont raise error
    print(e)


print("the program is executed :) without any crash")  # print program completed