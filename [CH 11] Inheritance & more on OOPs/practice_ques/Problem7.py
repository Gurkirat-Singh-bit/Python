# Problem 7) Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:                        # intialising a class vector

    def __init__(self, l):           # intialised a constuctor with arg. list
 
        self.l = l                   

    def __len__(self):               # overloading len for returning the len of vector

        return len(self.l)           # returning


v1 = Vector([10,20,30])              # taking a vector


print(len(v1))                       # printing the length