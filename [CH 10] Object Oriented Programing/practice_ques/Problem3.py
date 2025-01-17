# Problem 3) Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:                      # defining a class

    a = 5                        # class attribute

g = Demo()                       # obejct instance

g.a = 0                          # instance attribute

print(g.a)                       # printing instance attribute

print(Demo.a)                    # printing class attribute

# the answer is class attribute dont change because change are done for a particular object not for whole class