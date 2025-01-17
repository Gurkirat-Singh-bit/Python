# here i learnt what is a static method in python

class employee:                                # Define a class named 'employee'

    language = "python "                       # Class attribute

    salary = 10000000                          # Class attribute

    @staticmethod                              # Decorator to define a static method will dicuss decoraters later

    def greet():                               # Define a static method named 'greet'

        print("Good Morning")                  # Print "Good Morning"

# static method is a method that does not take 'self' as a parameter
# and does not have access to the instance of the class
# it is just a function that is defined inside a class
# it is used when we do not need to access the instance of the class

employee1 = employee()                         # Create an instance of 'employee' named 'employee1'

employee1.greet()                              # Call the static method 'greet' of 'employee1'