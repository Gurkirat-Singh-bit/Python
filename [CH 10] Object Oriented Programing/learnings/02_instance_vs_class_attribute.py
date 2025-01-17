# here i learnt difference between instance attribute and class attribute

class employee:                               # Define a class named 'employee'

    language = "python "                      # Class attribute 

    salary = 10000000                         # Class attribute

employee1 = employee()                        # Create an instance of 'employee' named 'employee1'

employee.language = "c++"                     # Assign the value "c++" to the class attribute 'language'

print(employee1.salary, employee1.language)   # Print the salary and language of 'employee1'

# instance attribute get more priority than class attribute

# while assigning as well as retrieving the value of an attribute

# if there is no instance attribute then class attribute is used by default