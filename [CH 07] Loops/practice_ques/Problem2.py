# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# list = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]                      # given list
 
for i in l:                                                    # intialising loop for list

    if(i.startswith("S")):                                     # if i starts with "s" then execute code blocks

        print(f"Hi ! {i}, Nice to see you")                    # if statement is true then it prints this