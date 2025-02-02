# here i learnt walrus operator in python

# how we normal solve these types of problem

lst = [1,2,3,4,5]

n = len(lst)

if n > 3:                                                    # 4 lines of code and also bit messy

    print(f"List is too long ({n} elements, expected <= 3)")

# Using walrus operator

if (n := len([1, 2, 3, 4, 5])) > 3:                          # 2 lines of code and also 

    print(f"List is too long ({n} elements, expected <= 3)")

# The walrus operator (:=), introduced in Python 3.8, allows you to assign values to 
# variables as part of an expression. This operator, named for its resemblance to the eyes 
# and tusks of a walrus, is officially called the "assignment expression."