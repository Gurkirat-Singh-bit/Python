# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random                               # importing random module

def game():                                 # defining a function game    
    
    print("you are playing game .....")     # printing playig game

    score = random.randint(1,100)           # generating a random number between 1 and 100

    print(f"Your score is {score}")         # printing the score
    
    f = open("Hi-score.txt")                # opening the file Hi-score.txt in read mode

    Hi_score = int(f.readline())            # reading the first line of the file and storing it in Hi_score also readline store in str


    if(Hi_score != 0):                      # checking if Hi_score is not equal to 0
 
        if(score > Hi_score):               # checking if score is greater than Hi_score

            f = open("Hi-score.txt", "w")   # opening the file Hi-score.txt in write mode

            f.write(str(score))             # writing the score in the file

    elif(Hi_score == 0):                    # checking if Hi_score is equal to 0
        
        f.write(str(score))                 # writing the score in the file

    f.close()                               # closing the file



game()                                      # calling the function game

