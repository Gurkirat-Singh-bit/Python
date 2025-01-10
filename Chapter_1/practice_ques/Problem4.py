# Problem 4). Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 


import os

# Specify the directory you want to list
directory_path = '/'  # Current directory (you can replace with any directory path)

# Get the list of contents in the directory
contents = os.listdir(directory_path)

# Print the contents of the directory
print("Contents of the directory:", directory_path)
for item in contents:
    print(item)
