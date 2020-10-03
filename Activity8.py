"""
Given a list of numbers, return True if first and last number of a list is same.
Bonus points if you can make the user enter their own list.
"""
numbers=list(input("Enter list of numbers: ").split(","))
print(numbers)
""" get first no"""
fnum=numbers[0]
"""get last no"""
lnum=numbers[-1]

if(fnum==lnum):
    print(True)
else:
    print(False)