# Problem 3) A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”.
#  Write a program to detect these spams.

spam1 = "Make a lot of money"
spam2 = "buy now"                                    # intialising the string as comman spam lines
spam3 = "subscribe this"
spam4 = "click this"

message = input("ENTER YOUR COMMENT : ")             # let user to comment

if((spam1 in message) or (spam2 in message) or (spam3 in message) or (spam4 in message)):
    print("PLEASE DON'T POST THESE TYPES OF COMMENTS")
    # REMOVE THIS MESSAGE                            # checked whether any spam string is detected or not