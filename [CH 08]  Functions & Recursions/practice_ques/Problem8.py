# Problem 8) Write a python function to print multiplication table of a given number.

def table(num):                                            # functions for printing the table 

    for i in range(11):                                    # for loop for printing table

        print(f"{num} X {i} = {num*1}")                 

num = int(input("ENTER NUMBER WHOSE TABLE YOU WANT : "))   # taking the number from the user 

table(num)                                                 # calling functions      