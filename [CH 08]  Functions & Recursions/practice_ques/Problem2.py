# Problem 2) Write a python program using function to convert Celsius to Fahrenheit.

# F = (C * 9/5) + 32

def cel_to_far(temp):                                             # function to convert celcius to fahrenheit

    return (temp * 9/5) + 32                                      # return the value of temp

temp = float(input("ENTER THE TEMPERATURE IN CELCIUS : "))        # taking input from the user

tempF = cel_to_far(temp)                                          # storing value recived from function

print(f"{temp}°C is {round(tempF, 2)}°F")                         # printing the convertion