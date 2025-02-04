# Problem 4) Write a program to filter a list of numbers which are divisible by 5.
 
def divby5(n):                                             # declaring function for checking whether number 

    if n%5==0:                                             # is div. by 5 or not

        return True                                      
    
    return False

l =[1,2,3,4,5,6,7,8,9,10,15,76,2,478,54,85,95,60]          # normal lsit containing random element

filtered = filter(divby5,l)                                # using filter function filtering factor of 5 in list

print(list(filtered))                                      # printing the list