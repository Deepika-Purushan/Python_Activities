"""
Create a Python dictionary that contains a bunch of fruits and their prices.
Write a program that checks if a certain fruit is available or not.
"""

Fruits={
    "apple" : 100,
    "banana" : 50,
    "grapes" : 90
}

Customer_Need=input("Which fruit you are looking for:").lower()

if(Customer_Need in Fruits):
    print("Yes, its available")
else:
    print("No, its not available")