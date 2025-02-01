# here i learnt the class method in python 

class demo:                                     # demo class created

    a = 1                                       # class attribute

    @classmethod                                # this method is used where we have to bound class attribute not object attribute

    def show(cls):                              # instead of self we use cls

        print(f"the value of a is {cls.a}")     # printing the object attribute 

e = demo()                                      # intialising a class object

e.a = 100                                       # assigning the value to object attribute

e.show()                                        # calling the method 