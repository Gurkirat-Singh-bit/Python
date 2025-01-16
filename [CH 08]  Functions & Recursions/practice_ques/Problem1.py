# Problem 1) Write a program using functions to find greatest of three numbers.

def greatest_three(n1,n2,n3):                           # function for greates of three

    if(n1>n2 and n1>3):
        return n2
    
    if(n2>n1 and n2>3):
        return n2
    
    if(n3>n2 and n3>n1):
        return n3
    
n1 = int(input("ENTER YOUR NUMBER : ")) 
    
n2 = int(input("ENTER YOUR NUMBER : "))                 # taking input from the user 
     
n3 = int(input("ENTER YOUR NUMBER : "))

print(f"THE NUMBER WHICH IS GREATEST AMOUNGEST THEM IS {greatest_three(n1,n2,n3)}")  # and printing it as well as calling functions