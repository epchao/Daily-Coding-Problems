# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?
#Attempts: Looked up, but understands how it works.
from functools import reduce

test_arr = [1, 2, 3, 4, 5]

def solver(arr):
  result = []
  for i, el in enumerate(arr):
    result.append(reduce(lambda x, y: x*y, arr[:i] + arr[i+1:]))
  return result

print(solver(test_arr))