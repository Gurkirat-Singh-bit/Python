# Problem 1) Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

dictionary = {
   "namaste" : "hello",
   "udhar" : "there",                                                       # intialising a small dictionary
   "kutta" : "dog",
   "kagaj" : "paper"

}

word = input("Enter the word you want to search in this dictionary : ")     # taking word from the user (key)
 
print(f"the meaning of {word} is {dictionary.get(word)} in english")        # printing the word's meaning (value)