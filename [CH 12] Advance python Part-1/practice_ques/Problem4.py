# Problem 4) Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’.

a = int(input("ENTER A NUMBER: "))                 # taking number from the user 

b = int(input("ENTER A NUMBER: "))
 
try:                                             # try block for trying the if condition works

    print(a/b)                                   # printing the answer

except ZeroDivisionError:                        # if divided by zero 

    print("infinite")                            # print infinte
