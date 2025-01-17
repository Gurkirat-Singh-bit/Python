# Problem 3) Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13_year old.

def tableprint(n):                                         # Function to print the table of n
     
     with open(f"Math_tables/Table_of_{n}", "w") as f:     # Opening the file in write mode
          
          f.write(f"THE TABLE OF {n} : \n")                # Writing the table of n

          for i in range(1,11):                            # Loop to print the table of n
               
               f.write(f"{n} X {i} = {n*i}\n")             # Writing the table of n in the file

for i in range(2,21):                                      # Loop to generate tables from 2 to 20
     
     tableprint(i)                                         # Calling the function to print the table of i