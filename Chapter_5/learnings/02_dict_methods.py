# here i learnt methods of dictinary in python

marks = {

     "gurkirat": 91,           
     "anc": 99,                              # example of marks using dictinory in python 
     "harshit": 67,
     "vansh": 78,
     "guarav": 88

}


print(marks.items())                         # get items in form of tuple(dict item actually)

print(type(marks.items()))                   # proving the type of dict item which is dict_item


print(marks.keys())                          # string.keys is used for getting all the key there in dictinary

print(type(marks.keys()))                    # this returns its type that is dict_keys


print(marks.values())                        # string.values is used to get all the values present in dictinary

print(type(marks.values()))                  # this returns its type that is dict_values


marks.update({"guarav": 91,"gulshan":45})    # string.update is used for updating the dictionary

print(marks)                                 # since dictinary is mutable the values are updated

print(marks.get("gulshan"))                  # used to get value of particular key the main difference between
                                             # marks["gulshan"] is .get returns 'None' while 
print(marks.get("kirat"))                    # marks["gulshan"] returns error


print(len(marks))                            # retuns the no. of key value pair present in dictionary
 
marks.clear()                                # clears the dictionary or removes everything

print(marks)                                 # result = empty dictionary

# and much more 