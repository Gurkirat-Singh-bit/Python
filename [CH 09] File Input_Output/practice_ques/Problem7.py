# Problem 7) Write a program to find out the line number where python is present from ques 6.

with open("essay.txt") as f:                                                     # opening file that we want to search keyword

    lines = f.readlines()                                                        # storing lines in variable

    line_no = 1                                                                  # line counter

    for line in lines:                                                           # loop to line to lines

        if("python" in line):                                                    # if line contain keyword

            print(f"yes this file contain word python at page no. {line_no}")    # print it contains

            break                                                                # and break from loop
        
        line_no += 1                                                             # increment the counter

    else:                                                                        # if , if condition is not true 

        print("file does not contain word python")                               # then print it does contain 