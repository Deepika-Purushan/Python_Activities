"""
Write a function sum() such that it can accept a list of elements and print the sum of all elements
"""
def cal_sum(number):
    sum = 0
    for num in number:
        sum+= num
    return sum
        
num_list=[1,2,3,4]
Final_sum = cal_sum(num_list)
print(Final_sum)
