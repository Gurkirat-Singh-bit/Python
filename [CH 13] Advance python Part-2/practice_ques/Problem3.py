# Problem 3) A list contains the multiplication table of 7. write a program to convert it to vertical 
# string of same numbers.

table = [str(7*i) for i in range(1,11)]           # storing the table of 7 in a list table

v_table = "\n".join(table)                        # using join function for  adding next line after each element
 
print(v_table)                                    # printing the table