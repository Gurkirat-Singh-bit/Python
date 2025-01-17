# here i learnt about __init__ method in python

class employee:                               # Define a class named 'employee'


    def __init__(self):                       # __init__ is a special method in python that is called when an object is created

        print("Program i created an object of employee class")  

        # these type of methods are called dunder methods in python. duner stands for double underscore

        # __init__ is also called a constructor because it is used to construct objects

    def __init__(self, name, salary, language):

        self.name = name                       # Assign the value of 'name' to the instance attribute 'name'

        self.salary = salary                   # Assign the value of 'salary' to the instance attribute 'salary'

        self.language = language               # Assign the value of 'language' to the instance attribute 'language'

        print("Program i created an object of employee class")  

        # we can have multiple __init__ methods in a class
        # but only the last __init__ method is executed

        # this is because the last __init__ method overwrites the previous __init__ methods

        # so we can only have one __init__ method in a class

        # if we want to have multiple __init__ methods we can use default arguments

        # we will discuss default arguments later

    

employee1 = employee("gurkirat singh", 10000000, "python")  # Create an instance of 'employee' named 'employee1'

print(employee1.name, employee1.salary, employee1.language) # Print the name, salary and language of 'employee1'

employee2 = employee("rohan sharma", 200000, "c++")         # Create another instance of 'employee' named 'employee2'

print(employee2.name, employee2.salary, employee2.language) # Print the name, salary and language of 'employee2'