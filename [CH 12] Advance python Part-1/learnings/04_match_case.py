# here i learnt match case in python

def http_status(status):                   # declaring a function

    match status:                          # using match case 

        case 200:                          # going to through different option
            return "ok"
        
        case 404:
            return "error page not found"
        
        case 500:
            return "internal server error found"
        
        case _:                            # base case or default case if none of the option executed it will defaulty executed
            return "unknown error"
        

print(http_status(500))                       # calling the function with an argument

# Python 3.10 introduced the match statement, which is similar to the switch statement 
# found in other programming languages. 
# The basic syntax of the match statement involves matching a variable against several 
# cases using the case keyword.