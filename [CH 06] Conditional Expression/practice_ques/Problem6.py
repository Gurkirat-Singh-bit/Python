# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme:
# 90 – 100 => Ex
# 80 – 90  => A
# 70 – 80  => B
# 60 – 70  => C
# 50 – 60  => D
# <50      => F

marks = float(input("ENTER YOUR MARKS : "))                 # TAKING MARKS FROM THE USER 

if(marks>100):                                              # BY GIVING SCHEME USING IF AND ELIF
    print("PLEASE ENTER VAILD MARKS")                       # ACORDINGLY

elif(marks<0 ):
    print("PLEASE DONT ENTER A  NEGATIVE MARKS ")

elif(marks<=100 and marks>=91):
    print("YOU GOT EXELENT GRADE")

elif(marks<=90 and marks>=81):
    print("YOU GOT A GRADE")

elif(marks<=80 and marks>=71):
    print("YOU GOT B GRADE")

elif(marks<=70 and marks>=61):
    print("YOU GOT C GRADE")

elif(marks<=60 and marks>=50):
    print("YOU GOT D GRADE")

elif(marks<=49):
    print("YOU UNABLE TO PASS THE EXAM")