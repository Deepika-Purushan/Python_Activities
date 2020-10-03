"""
Given a tuple of numbers, iterate through it and print only those numbers which are divisible by 5
    Bonus points if you can make the user enter their own tuple.
"""
numbers=tuple(input("Enter list of numbers: ").split(","))
print(numbers)

for num in numbers:
    if (int(num) % 5 == 0):
        print("Numbers which are divisible by 5:", num)
