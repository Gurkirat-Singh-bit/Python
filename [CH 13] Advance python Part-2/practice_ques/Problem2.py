# Problem 2) Write a program to input name, marks and phone number of a student and format it
# using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”
 
name = input("Enter your name : ")                                # taking name from the user

marks = float(input("Enter your marks : "))                       # taking marks from the user

mobile_no = int(input("Enter your mobile or phone number : "))    # taking mobile_no. from the user


print("The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,mobile_no))

# printing the given stuff using .format function as given in the problem