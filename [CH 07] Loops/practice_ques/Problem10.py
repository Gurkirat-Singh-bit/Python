# Problem 10) Write a program to print multiplication table of n using for loops in reversed order


num = int(input("ENTER THE NUMBER , WHOSE TABLE YOU WANT : "))       # taking number from the user

v = 10                                                               # counter from 10 to 1

while(v>0):                                                          # while loop going to zero

    print(f"{num} X {v} = {num*v}")                                  # printing the table

    v -= 1                                                           # updating counter