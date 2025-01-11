# Problem 2) Write a program to fill in a letter template given below with name and date.

# letter = '''Dear <|Name|>, You are selected!<|Date|>'''

letter = '''  Dear <|Name|> , You are selected! <|Date|>'''

print(letter.replace("<|Name|>","Gurkirat Singh").replace("<|Date|>","11 january 2026"))

# using string replace function and replaced name and then from same string date