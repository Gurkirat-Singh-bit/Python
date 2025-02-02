# Problem 2) Write a program to print third, fifth and seventh element from a 
# list using enumerate function.

lst = [1,2,3,4,5,6,7,8,9]        # a list

for i,item in enumerate(lst):    # using enumerate to access all list elements

    if i==2 or i==4 or i==6:     # condtion for 3rd , 5th and 7th element of list

        print(f"{i}--> {item}")  # printing
    