# here i learnt IF __NAME__== ‘__MAIN__’ IN PYTHON

from module import myfunc

myfunc()


# ‘__name__’ evaluates to the name of the module in python from where the program is ran.

# If the module is being run directly from the command line, the ‘ __name__’ is set to 
# string “__main__”. Thus, this behaviour is used to check whether the module is run 
# directly or imported to another file.
