"""
Write a Python program to calculate the sum of all the elements in a list.
Bonus points if you can make the user enter their own list.
"""
numbers=list(input("Enter list of numbers: ").split(","))
print(numbers)

sum=0

for num in numbers:
    sum +=int(num)
print(sum)