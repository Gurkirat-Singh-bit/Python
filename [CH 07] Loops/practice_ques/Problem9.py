# Problem 9. Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * *

n = int(input("enter number please : "))

for i in range(1,n+1):

    if(i==1 or i==n):

        print("*"* n)

    else:
         print("*", end="")

         print(" "*(n-2), end="")

         print("*", end="")
         
         print("")
        