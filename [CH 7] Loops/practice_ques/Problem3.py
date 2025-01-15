# Problem 3) Write a program to print multiplication table of a given number using while loop

num = int(input("ENTER THE NUMBER , WHOSE TABLE YOU WANT : "))       # taking number from the user

i = 1

while(i<11):
    print(f"{num} X {i} = {num*i}")
    i += 1