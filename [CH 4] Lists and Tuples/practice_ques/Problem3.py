# Problem 3) To check that a tuple type can be changed in python or not.

tuple = (1,23,3,"fool",'suiiiiiiiiiii')         # intialising tuple

tuple[2] = "larry"                              # trying to make change in tuple


# Result : no we can't tuple is unmutable

# Proof:
# PS K:\Python\CODE> & C:/Users/Gurki/AppData/Local/Programs/Python/Python312/python.exe k:/Python/CODE/Chapter_4/practice_ques/Problem3.py
# Traceback (most recent call last):
#   File "k:\Python\CODE\Chapter_4\practice_ques\Problem3.py", line 5, in <module>
#     tuple[2] = "larry"
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment