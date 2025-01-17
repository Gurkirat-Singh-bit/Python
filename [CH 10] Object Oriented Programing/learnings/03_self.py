# here i learnt self parameter in python

class employee:                                # Define a class named 'employee'
    
    language = "python "                       # Class attribute 

    salary = 10000000                          # Class attribute

    def printdetails(self):                    # Define a method named 'printdetails' with 'self' as a parameter

        print(f"language is {self.language}")  # Print the language of the instance

        print(f"salary is {self.salary}")      # Print the salary of the instance

    def greet(self):                           # Define a method named 'greet' with 'self' as a parameter

        print("Good Morning")                  # Print "Good Morning"

        # even though this method does not use the 'self' parameter it is necessary to include it
        # because it is a method of the class 'employee' and 
        # all methods of a class must have 'self' as a parameter
        # self is just a convention and can be replaced with any other name
        # but we usually use 'self' as a parameter


employee1 = employee()                         # Create an instance of 'employee' named 'employee1'

employee1.language = "c++"                     # Assign the value "c++" to the instance attribute 'language'

employee1.printdetails()                       # Call the method 'printdetails' of 'employee1'

employee1.greet()                              # Call the method 'greet' of 'employee1'


# self is a parameter that refers to the instance of the class
