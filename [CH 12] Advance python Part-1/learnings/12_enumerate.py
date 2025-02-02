# here i learnt ENUMERATE FUNCTION IN PYTHON

lst = [1,2,3,4,5,6,7,8,9]                 # A list


i1 = 0                                    # iterator for list  

for item in lst:

    print(f"{i1}. {item}")               # normal method 4 line of code also bit messy

    i1 += 1

print("\n\n")                            # for gap

for i , _item in enumerate(lst):         # using enumerate doing same thing with 2 line of code

    print(f"{i}. {_item}")