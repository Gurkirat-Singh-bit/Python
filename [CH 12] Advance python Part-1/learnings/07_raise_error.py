# here i learnt how to raise error in python   -_-

num1 = int(input("Enter a number : "))

num2 = int(input("Enter a number : "))

if num2==0:                             # rassing error if a condition is true

    raise ZeroDivisionError("fuck you bro why you divide something with zero")  # this stop(crash) program

print(f"The division of num1/num2 is {num1/num2}")