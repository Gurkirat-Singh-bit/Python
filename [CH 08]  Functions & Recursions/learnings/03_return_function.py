# here i learnt the use case of return in function

def avg(n1,n2,n3):                                                 # function defination for finding average

    avg = (n1+n2+n3)/3                                             # average is sum of number divided by 3 

    return avg                                                     # return avg which contain average value
 

n1 = int(input("ENTER NUMBER : "))

n2 = int(input("ENTER NUMBER : "))                                 # taking input from the user

n3 = int(input("ENTER NUMBER : "))

print(f"THE AVERAGE OF THE GIVEN NUMBERS ARE {avg(n1,n2,n3)}")     # printing the average of three numbers