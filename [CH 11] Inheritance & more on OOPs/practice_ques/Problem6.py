# Problem 6) Write __str__() method to print the vector as follows:
#  7i + 8j +10k 
# Assume vector of dimension 3 for this problem.
# Problem 5) Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them.

class Vector:                                 # class for vector

    def __init__(self, i , j , k):            # constructor for vector 

        self.i = i
        self.j = j 
        self.k = k

    def __add__(self, v2):                    # overloading add to add vector

        return Vector(self.i + v2.i , self.j + v2.j ,self.k + v2.k)
    
    def __mul__(self, v2):                    # overloading multiply for multiplying vector

        i_part = self.i * v2.i
        j_part = self.j * v2.j
        k_part = self.k * v2.k

        return Vector(i_part , j_part , k_part)     
    
    def __str__(self):                        # overloading string for displaying vector

        return f"VECTOR is {self.i}i + {self.j}j + {self.k}k "
    

    

v1 = Vector(10,20,30)                          # intialising vector 1
                                              
v2 = Vector(30,20,10)                          # intialising vector 2
 
print(v1+v2)                                   # adding vector

print(v1*v2)                                   # mutliplying vector