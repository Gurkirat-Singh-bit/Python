# Problem 6) Write a program to calculate the factorial of a given number using for loop.

fact = 1                                      # intialising fact as one for storing factorial
 
num = int(input("enter number : "))           # taking input from the user

for i in range(1,num+1):                      # intialising loop till num 

    fact *= i                                 # mutiplying the factorial to n and storing it

    i += 1                                    # iteration update
 
print(f"the factorial {num} is {fact}")       # printing the factorial