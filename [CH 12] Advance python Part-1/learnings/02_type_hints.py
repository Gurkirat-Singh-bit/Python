# here i learnt type hints in python


n : int = 5                                 # telling python that this is a integer

name : str = "gurkirat singh"               # telling python that this is a string


def sum (a:int,b:int) -> int:               # function in which we tell python that it takes two integer 

    print(n := a+b)                         # printing as well assigning sum 

    print(type(n))                          # printing its types


a,b = 1,2                                   # declaring varibles 

sum(a,b)                                    # calling the function
                    
# Type hints are added using the colon (:) syntax for variables and the -> syntax for 
# function return types2