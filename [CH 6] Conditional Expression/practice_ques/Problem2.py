# Problem 2) Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

s1 = float(input("ENTER SUBJECT 1 MARKS : "))

s2 = float(input("ENTER SUBJECT 2 MARKS : "))              # taking marks of subejct

s3 = float(input("ENTER SUBJECT 3 MARKS : "))

percentage = (s1+s2+s3)/3

if( percentage >= 40 and s1>=33 and s2>=33 and s3>=33):   # making condition that satisfy our need          
    print(f"congratulations!!! you passed the exam with {percentage}% of marks")

else: 
    print("sorry you unable to pass in the exam ; failed")