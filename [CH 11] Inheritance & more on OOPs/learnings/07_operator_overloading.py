# here i learnt operator overloading in python
    
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Create two Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Add two Point objects using the overloaded + operator
p3 = p1 + p2

print(p3)  # Output: (4, 6)