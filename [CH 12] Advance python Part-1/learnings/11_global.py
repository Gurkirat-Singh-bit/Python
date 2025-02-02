# here i learnt global keyword in python

a =  89                    # its is a global variable

def func():                # declaring a function

    global a               # changing a variable globally

    a = 3                  # the change
    
    print(a)               # printing a 


func()                     # calling func which makes to change a globally


print(a)                   # printing a