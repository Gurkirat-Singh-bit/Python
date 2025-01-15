# Problem 7) Write a program to find out whether a given post is talking about “Harry” or not.

post = input("POST HERE --> ")                       # taking post from the user

if("harry".lower() in post.lower()):                   # using .lower converting both side into lower case so that haRry kinds of keywords can be detected     

    print("this post is talking about Harry")        # printing if condition is true      


else:
    print("this post is not talking about harry")    # if post dont contains harry this will execute