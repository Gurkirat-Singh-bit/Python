# Problem 2)  Write a class “Calculator” capable of finding square, cube and square root of a number.

class calculator:                                            # defining a class

    def __init__(self, n):                                   # init function to get value automatically

        self.n = n                                           # taking parametr into attribute

    def square(name):                                        # function for printing square

        print(f"square of {name.n} is {name.n*name.n}") 

    def cube(name):                                          # function for printing cube
 
        print(f"cube of {name.n} is {name.n*name.n*name.n}")

    def square_root(name):                                   # function for printing square root 

        print(f"square_root of {name.n} is {name.n**1/2}")

a = calculator(3)                                            # making an object

a.square()                                                   # calling function

a.cube()                                                     # calling function

a.square_root()                                              # calling function