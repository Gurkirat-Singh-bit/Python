# here i learnt try with finally in python

# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of 
# the exception.

try:                                                      # try check whether things works or not
 
    print(num :=  int(input("Enter a number :")))


except Exception as e:                                    # if not dont raise error

    print(e)

finally:                                                  # if everything is runned properly this will execute

    print("block executed no matter what is done i am sigma finally 🗿")


print("the program is executed :) without any crash")     # print program completed