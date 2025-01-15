# Problem 1) Write a program to print multiplication table of a given number using for loop.

num = int(input("ENTER THE NUMBER , WHOSE TABLE YOU WANT : "))       # taking number from the user

for i in range(num+1):                                                  # taking loop to repeate itself 10 time

    print(f"{num} X {i} = {num*i}")                              # print the table
 
