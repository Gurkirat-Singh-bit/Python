# Problem 5) Write a program to find the sum of first n natural numbers using while loop.

sum = 0                                        # intialising a sum for storing the value 

i = 1                                          # intialisng a counter i

num = int(input("enter your number : "))       # taking the number from the user from 

while(i<num+1):                                # while loop to num 

    sum += i                                   # adding i into sum 

    i += 1                                     # updating i 

print(f"the sum is {sum}")                     # printing the sum at last