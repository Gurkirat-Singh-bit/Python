# here i learnt dictinary merge and update operators in pythons

# Old Method (Pre-Python 3.9)

dict1_old = {'a': 1, 'b': 2}
dict2_old = {'b': 3, 'c': 4}

# Merging dictionaries using .update()
dict1_old.update(dict2_old)
print("Old method (merged):", dict1_old)  # {'a': 1, 'b': 3, 'c': 4}

# Updating dictionary using .update()
dict1_old.update({'b': 3, 'c': 4})
print("Old method (updated):", dict1_old)  # {'a': 1, 'b': 3, 'c': 4}


# New Method (Python 3.9+)

dict1_new = {'a': 1, 'b': 2}
dict2_new = {'b': 3, 'c': 4}

# Merging dictionaries using | operator (creates a new dictionary)
merged_dict = dict1_new | dict2_new
print("New method (merged):", merged_dict)  # {'a': 1, 'b': 3, 'c': 4}

# Updating dictionary using |= operator (modifies the original dictionary)
dict1_new |= {'b': 3, 'c': 4}
print("New method (updated):", dict1_new)  # {'a': 1, 'b': 3, 'c': 4}
