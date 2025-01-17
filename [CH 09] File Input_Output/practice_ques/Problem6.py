# Problem 6) Write a program to mine a log file and find out whether it contains ‘python’.

with open("log.txt") as f:

    contents = f.read()

    if("python" in contents or "Python" in contents):

        print("this log file contain word python")

    else:
        
        print("this log file does not contain word python")
