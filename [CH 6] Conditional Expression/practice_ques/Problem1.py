# Problem 1) Write a program to find the greatest of four numbers entered by the user.

a1 = int(input("ENTER A NUMBER : "))
a2 = int(input("ENTER A NUMBER : "))               # taking diffrent number from the user 
a3 = int(input("ENTER A NUMBER : "))
a4 = int(input("ENTER A NUMBER : "))

if(a1>a2 and a1>a3 and a1>a4):
    print(f"{a1} is greatest amoung all")

elif(a2>a1 and a2>a3 and a2>a4):
    print(f"{a2} is greatest amoung all")         # using if and elif checking which number is greatest amoung them

elif(a3>a2 and a3>a1 and a3>a4):
    print(f"{a3} is greatest amoung all")

elif(a4>a2 and a4>a3 and a4>a2):
    print(f"{a4} is greatest amoung all")