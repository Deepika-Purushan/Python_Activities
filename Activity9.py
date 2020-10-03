"""Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list 
and even numbers from the second list."""

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[11,12,13,14,15,16,17,18,19,20]

print("First list: ", list1)
print("Second List: ", list2)

list3 = []

for num in list1:
    if(num % 2 != 0):
        list3.append(num)

for num in list2:
    if(num % 2 == 0):
        list3.append(num)
 
print("Result List is:", list3)
    
