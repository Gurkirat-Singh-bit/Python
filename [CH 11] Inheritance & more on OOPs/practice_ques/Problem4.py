# Problem 4) Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them

class Complex():                                # intialising class for complex number

    def __init__(self,r,i):                     # constructor for taking the value of complex number

        self.r = r
        self.i = i
     
    def __add__(self, c2):                       # overloading add  for adding complex number  

        return Complex(self.r + c2.r , self.i + c2.i)
    
    def __mul__(self,c2):                        # overloading mul for return multiplying  complex  number

        realpart = self.r * c2.r
    
        im_part = self.i * c2.i

        return Complex(realpart,im_part)

    def __str__(self):                           # overloading string for return complex 

        return f"{self.r} + {self.i}i"
    
c1 = Complex(12,23)                              # complex number 1

c2 = Complex(130,243)                            # complex number 2
 
print(c1+c2)                                     # adding complex number

print(c1*c2)                                     # multiplying complex number