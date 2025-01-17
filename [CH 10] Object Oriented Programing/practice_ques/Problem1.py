# Problem 1) Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:                                               # Define a class named Programmer

    def __init__(self, name, age, experience, language):        # Initialize the class with name, age, experience, and language attributes

        self.name = name                                        # Assign the name parameter to the name attribute

        self.age = age                                          # Assign the age parameter to the age attribute

        self.experience = experience                            # Assign the experience parameter to the experience attribute

        self.language = language                                # Assign the language parameter to the language attribute
        
        print(f"The detail of {name} is saved")                 # Print a message indicating that the details of the programmer are saved


Programmer1 = Programmer("gurkirat singh", 17, "0year", "python")  # Create an instance of the Programmer class with specific details

Programmer2 = Programmer("vansh", 16, "0year", "HTML")             # Create another instance of the Programmer class with specific details
