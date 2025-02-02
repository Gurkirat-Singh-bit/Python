# here i learnt try with else  in python 

try:                                                    # try check whether things works or not

    print(num :=  int(input("Enter a number :")))


except Exception as e:                                 # if not dont raise error

    print(e)

else:                                                  # if everything is runned properly this will execute

    print("block executed with no exception")


print("the program is executed :) without any crash")  # print program completed