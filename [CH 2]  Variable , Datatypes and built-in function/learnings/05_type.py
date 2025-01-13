# here we learn how to print type of variable and converting one datatype to other

# how i find the datatype of variable

a = 1
b = 2.01
c = "gurkirat"
d = True
e = None

A = type(a)
B = type(b)          # type is used for finding the datatype of variable
C = type(c)  
D = type(d)
E = type(e)

print(A,B,C,D,E)     # printing the data type assigned to A, B, C, D, E

# Converting one datatype into other 

a = "12"        # like here a is string 
A = int(a)      # by using 'int'as function , a is converted into float
print(type(A))  # here through the output i checked the type of A which should be int

a = "1.99999"   # like here a is string 
A = float(a)    # by using 'float'as function , a is converted into float
print(type(A))  # here through the output i checked the type of A which should be float

# a = "13.333"      like here a is string 
# A = int(a)        but i am trying to convert float capable data into integer
# print(type(A))    which is not possible in python