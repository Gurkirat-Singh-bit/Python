# Problem 2) Write a program to input eight numbers from the user and display all the unique numbers (once)

s = set()                                          # intialising an empty set 



n = int(input("enter your number : "))
s.add(n)

n = int(input("enter your number : "))
s.add(n)

n = int(input("enter your number : "))             # taking the number from the user by explicit conversion
s.add(n)                                           # so that we get number not strings

n = int(input("enter your number : "))
s.add(n)

n = int(input("enter your number : "))
s.add(n)

n = int(input("enter your number : "))
s.add(n)

n = int(input("enter your number : "))
s.add(n)

n = int(input("enter your number : "))
s.add(n)

print(s)                                            # printing the final set that is going to be used here