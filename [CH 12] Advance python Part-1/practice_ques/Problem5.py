# Problem 5) Store the multiplication tables generated in problem 3 in a file named Tables.txt

try:                                                                # try if user enter something incorrect

    num = int(input("Enter the number, whose table you want : "))   # taking input from the user

    table = [num*i for i in range(1,11)]                            # using list comprehension

    print(table)                                                    # printing the table list

    with open("Tables.txt", "a") as f:

        f.write(str(table))
        

except Exception as e:                                              # if any exception 

    print("SOMETHING WENT WRONG")                                   # print this