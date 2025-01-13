# here i learnt how to slice a string

# Positive Slicng

Name = "Gurkirat Singh"           # intialise string

Nameshort = Name[0:9]             # slicing the string

# started from 0 till 9 excluding 9
  
print(Nameshort)                  # printing the sliced string

# here it removes my surname and only display my name 

Char = Name[0]                    # printing my first letter of my name

# started from 0 and ends on 0 i.e  only one digit

print(Char)                       # printing the first character of my name

# by this we can print any character from string

#  Name = G u r k i r a t   S  i  n  g  h
#         0 1 2 3 4 5 6 7 8 9 10 11 12  13
#         ................-5 -4 -3  -2  -1

# Negative Slicing 

NegName = Name[-14:-5]            # negatively sliced the string

print(NegName)                    # printing negative sliced string


print(Name[:8])                   # same as printing from 0 to 8

print(Name[8:])                   # same as printing from  8 to 13

# String Slicing by skipping the value

print(Name[0:8:3])                # staring from 0 to 8 and then skiping every 3 (printing the third)

# here result will be Gka