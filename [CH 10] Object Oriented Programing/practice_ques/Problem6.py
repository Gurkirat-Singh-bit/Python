# Problem 6) Can you change the self-parameter inside a class to something else (say“harry”).
#  Try changing self to “slf” or “harry” and see the effects

class demo:                         # defining a class

    def __init__(sl,name):          # using sl instead of self as parameter

        sl.name = name              # class attribute

        print(name)                 # printing name



a = demo("gurkirat singh")          # no error is genrated program works with any parameter