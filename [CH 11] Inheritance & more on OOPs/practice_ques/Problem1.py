# Problem 1) Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twoDvector:
    def __init__(self, i, j):

        self.i = i

        self.j = j

    def show(self):

        print(f"the 2D vector is {self.i}i + {self.j}j")

class threeDvector(twoDvector):

    def __init__(self, i, j, k):

        super().__init__(i , j)

        self.k = k

    def show(self):

        print(f"the 3D vector is {self.i}i + {self.j}j + {self.k}k")

vector_1 = twoDvector(1,3)

vector_1.show()

vector_2 = threeDvector(2 , 4 , 5)

vector_2.show()
