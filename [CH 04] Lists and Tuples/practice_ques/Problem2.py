# Problem 2) Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

m1 = int(input("enter marks"))
marks.append(m1)

m2 = int(input("enter marks"))
marks.append(m2)

m3 = int(input("enter marks"))                            # taking marks from the user
marks.append(m3)                                          # rember input take anthing as string
                                                          # so we done explicit conversion into int
m4 = int(input("enter marks"))               
marks.append(m4)

m5 = int(input("enter marks"))
marks.append(m5)

m6 = int(input("enter marks"))
marks.append(m6)

m7 = int(input("enter marks"))
marks.append(m7)

marks.sort()                                              # sorting the list using sort function

print(marks)                                              # printing the list