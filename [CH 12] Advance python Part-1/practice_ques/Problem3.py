# Problem 3) Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number.

try:                                                                # try if user enter something incorrect

    num = int(input("Enter the number, whose table you want : "))   # taking input from the user

    table = [num*i for i in range(1,11)]                            # using list comprehension

    print(table)                                                    # printing the table list

except Exception as e:                                              # if any exception 

    print("SOMETHING WENT WRONG")                                   # print this
