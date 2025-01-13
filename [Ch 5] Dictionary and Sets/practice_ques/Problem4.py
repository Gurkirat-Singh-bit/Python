# Problem 4) What will be the length of following set s:

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')                                                   # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20')                                                     # length of s after these operations?

# the length of the set will be 2 beacuse 20 and 20.00 will be equal cause python recognize them as same and string is seperate 

print(len(s))                                                   # verifying my answer by printing its length