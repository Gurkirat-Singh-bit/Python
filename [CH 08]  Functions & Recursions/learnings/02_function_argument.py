# here i learnt functions with argument 

def gooday(name,time):                                # function decleration with argument required

    print(f"have a nice day {name}")                  # printing have a nice day with the name of the user 

    print(f"its {time} here")                         # printing time by using time argument


name = input('enter your name : ')                    # taking input from the user

time = input('enter time : ')                         # taking input from the user

gooday(name,time)                                     # functions call with given argument