"""
Write a recursive function to calculate the sum of numbers from 0 to 10
"""
def calSum(num):
  if num:
    return num + calSum(num-1)
  else:
    return 0

Sum = calSum(10)
print("Sum of 0 to 10:", Sum)        