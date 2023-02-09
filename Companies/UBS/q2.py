# Given an array of integers, determine the number of ways the entire array be split into two non- empty subarrays, left and right, such that the sum of elements in the left subarray is greater than the sum of elements in the right subarray.
# Example
# arr = [10, 4, -8, 7]
# There are three ways to split it into two non- empty subarrays:
# 1. [10] and [4, -8, 7], left sum = 10, right sum = 3 2. [10, 4] and [-8, 7], left sum = 10+4= 14, right sum =-8+7=-1
# 3. [10, 4, -8] and [7], left sum = 6, right sum = 7
# The first two satisfy the condition that left sum > right sum, so the return value should be 2.

#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'splitIntoTwo' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def splitIntoTwo(arr):
    # Write your code here
    
    n = len(arr)
    total_sum = sum(arr)
    prefix_sum = [0] * (n + 1)
  
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
        
    count = 0
    for i in range(1, n):
        if prefix_sum[i] > total_sum - prefix_sum[i]:
            count += 1
    return count
        

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(raw_input().strip())

#     arr = []

#     for _ in xrange(arr_count):
#         arr_item = int(raw_input().strip())
#         arr.append(arr_item)

#     result = splitIntoTwo(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
