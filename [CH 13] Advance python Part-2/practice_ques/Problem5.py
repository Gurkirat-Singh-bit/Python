# Problem 5) Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce               # importing reduce form functool

def larger(a,b):

    if a>b:

        return a                           # function for larger number
    
    elif a<b:

        return b
    
l = [1,2,34,0,4456,6,7,34,464,3,6774,643,35,63,64,673,366,532,33,973,34,346,2345,34]      # random number list

larger_num = reduce(larger,l)              # using reduce function finding largest number in the list

print(larger_num)                          # printing the larger number