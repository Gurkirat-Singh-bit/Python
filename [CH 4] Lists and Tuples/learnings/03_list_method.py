# here i learnt methods of list

friends = ["chatgpt","vansh","finch", 100]      
roll_no = [23,23,24,45,5,3,24,57,27,876,357,87,554,24,76]
friends.append("me")                                       # append() used to add data in the list from the end 
print(friends)

roll_no.sort()                                             # sort() used to sort the Number list only, in assending order
print(roll_no)

roll_no.reverse()                                          #  reverse() used to reverse the  list 
print(roll_no)

friends.reverse()                                          #  reverse() used to reverse the  list 
print(friends)

roll_no.insert(4,29)                                       # insert() used for inserting data in-between a list
print(roll_no)

friends.insert(4,"Anc")                                    # insert() used for inserting data in-between a list 
print(friends)

roll_no.pop(4)                                             # pop() used for deleting a data and returning it
print(roll_no)
print(roll_no.pop(4))

friends.pop(4)                                             # pop() used for deleting a data with its index and returning it
print(friends)
print(friends.pop(4))

roll_no.remove(5)                                          # remove() used for removing a data with its name and returning it
print(roll_no)

friends.remove("finch")                                     # remove() used for removing a data with its name and returning it
print(friends)

# and many more methods