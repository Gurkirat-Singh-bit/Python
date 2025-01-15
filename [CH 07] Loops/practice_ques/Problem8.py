# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

n = int(input("enter number please : "))

for i in range(1,n+1):

    print(" "* (n - i), end = "")

    print("*"*i, end = "")
    
    print("\n")