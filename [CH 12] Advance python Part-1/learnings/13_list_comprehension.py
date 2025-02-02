# here i learnt list comprehension in python

mylst = [1,2,3,4,5,6,7,8,9]           # a list

squaredlst = []

for item in mylst:                    # old method for doing these types of things

    squaredlst.append(item*item)      # uses 5 line of code 

print(squaredlst)

print("\n\n")

# List Comprehension is an elegant way to create lists based on existing lists

squaredlist = [i*i for i in mylst]    # use list comprehension 

print(squaredlist)                    # uses only 2 line of code