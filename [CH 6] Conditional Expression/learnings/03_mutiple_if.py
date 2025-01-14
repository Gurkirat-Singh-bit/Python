# here i learnt multiple if statements
# by previous example of checking whether user is adult of not by age (LITTLE MODIFICATION)


age = int(input("ENTER YOUR AGE  : "))                      # taking age from the user


# START OF IF STATEMENT 1

if(age%2==0):                                               # this "if" is seprate from rest

    print("WOW YOUR AGE IS EVEN")

# END OF IF STATEMENT 1

# onlt "if" can be used alone else and elif is not used alone

# START OF IF STATEMENT 2

if(age>=18):                                                # ths is 'if' condition used for condition

    print("YOU ARE ADULT")                                  # here its age>=18 if it true then it print adult


elif(age==0):                                               # this is elif used when we need mutiple conditions in the program

    print("PLEASE ENTER  A VAILD AGE")                      # here if the user enter 0 age then its print pls enter a vaild age


elif(age<0):  

    print("PLEASE ENTER A VAILD AGE NOT NEGATIVE AGE")      # here if the user enter 0 age then its print pls enter a vaild age
 

else:                                                       # this is else if the condition in "if" is false 

    print("YOU ARE NOT ADULT")                              # then it executes and print not adult

# END OF IF STATEMENT 2


print("END OF PROGRAM")                                     # this is not the part of the program