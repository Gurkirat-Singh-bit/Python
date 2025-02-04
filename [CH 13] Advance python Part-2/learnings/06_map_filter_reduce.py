# here i learnt map , reduce and filter in python 


from functools import reduce    # importing reduce from functools



# map

l = [1,2,3,4,5,6,7,8,9]         # normal ist

square = lambda x: x*x          # lambda function for square of number

sqlist = map(square, l)         # iterate over the list

print(list(sqlist))             # printing squared lsit

# filter

def even(n):                    # function

    if n%2==0:                  # for even numbers

        return True             # if number even it return true
    
    return False                # rest eveytime false

onlyeven = filter(even,l)       # filter; filter the even from list

print(list(onlyeven))           # print even list

# reduce
 
fact = lambda a,b: a*b          # lambda function for product

print(reduce(fact,l))           # here it find factorial of 9 i.e 362880