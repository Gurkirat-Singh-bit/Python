# here i learnt how to take input in python for user

a = input("enter first number  : ")    # input is used for taking the input from the user 
b = input("enter second number : ")    # in string datatype analyze sum result -_-

print("first number is : ", a)         # print first number taken from the user
print("second  number is : ", b)       # print second number taken from the user

print("sum of two number is ", a+b)    # important to analayze this result

# most probably i runned the program and analyze it that instead of printing the sum
# it combine the digits , for example if i add 12 and 32 instead of summing its 
# it give us 1232 because input function takes input as string , here string combined
# to solve this we have to use type converstion ; int(input())

A = int(input("enter first number"))   # as here i used int for type convertion of
B = int(input("enter Second number"))  # string into integer

print("sum of the two number is equal to ", A+B)    # here the actual sum printed