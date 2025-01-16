# Problem 6) Write a python function which converts inches to cms.
# 1 inche = 2.54cms

def inch_to_cm(inch):                                # function for converting inch to cm
 
    return inch * 2.54                               # conversion

inch = float(input("ENTER LENGTH IN INCHE ->"))      # taking INPUT FROM THE USER 

print(f"THE CONVERSION IS \n {inch} inches is equal to {inch_to_cm(inch)} cms") # PRINTING TEMPERATURE

