# Divide and Conquer: maximum subarray
#
# Problem: Given an unsorted array Arr with n integers, find the maximum sum
#          of contiguous elements among all the possible subarrays.
#   Input: Unsorted array Arr of length n and an integer k where 1≤k≤n
#  Output: The sum of the maximum subarray
#
# Example 1
#   Arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
#   Output = 10 (for subarray [5, 0, 3, 2])
#
# Example 2
#   Arr = [-2, -5, 6, -2, -3, 1, 5, -6]
#   Output = 7 (for subarray [6, -2, -3, 1, 5])
import math

def get_cross_sum(nums, left, right, p):

    if left == right:
        return nums[left]

    left_subsum = -math.inf
    curr_sum = 0
    for i in range(p, left - 1, -1):
        curr_sum += nums[i]
        left_subsum = max(left_subsum, curr_sum)

    right_subsum = -math.inf
    curr_sum = 0
    for i in range(p + 1, right + 1):
        curr_sum += nums[i]
        right_subsum = max(right_subsum, curr_sum)

    return left_subsum + right_subsum   

def helper(nums, left, right):

    if left == right:
        return nums[left]

    p = (left + right) // 2

    left_sum = helper(nums, left, p)
    right_sum = helper(nums, p + 1, right)
    cross_sum = get_cross_sum(nums, left, right, p)

    return max(left_sum, right_sum, cross_sum)

def maxSubArray(nums: 'List[int]') -> 'int':

    return helper(nums, 0, len(nums) - 1)

# Test cases
print('Testing Kth Largest Element solution')

# Test 1
Arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
Output = 10 # for [5, 0, 3, 2]
print('  Test 1: ' + 'Pass' if maxSubArray(Arr) == Output else 'Fail')

# Test 2
Arr = [-2, -5, 6, -2, -3, 1, 5, -6]
Output = 7 # for [6, -2, -3, 1, 5]
print('  Test 2: ' + 'Pass' if maxSubArray(Arr) == Output else 'Fail')

