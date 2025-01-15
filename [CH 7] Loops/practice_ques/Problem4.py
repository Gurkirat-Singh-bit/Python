# Problem 4) Write a program to find whether a given number is prime or not

num = int(input("enter number : "))                          # taking input from the user 

counter = 0                                                  # intialising a counter 
  
for i in range(1,num):                                       # loop till num 

    if( (num%i) == 0):                                       # if num is divided by a number

        counter += 1                                         # counter iterate by one
 
if(counter == 1 ):                                           # if counter is equal to 1

    print(f"the given number {num} is a prime number")       # print prime

else:                                                        # else 
                   
    print(f"the given number {num} is not a prime number")   # not prime