# Divide and Conquer: k_th largest element
#
# Problem: Given an unsorted array Arr with n positive integers, find the k_th
#          smallest element in the given array.
#   Input: Unsorted array Arr of length n and an integer k where 1≤k≤n
#  Output: The k_th smallest element of array Arr
#
# Example 1
#   Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
#   k = 10
#   Output = 99
#
# Example 2
#   Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
#   k = 5
#   Output = 12
from typing import List

def findMedian(Arr: List[int], start: int, size: int) -> int:
    '''
    Helper function for find the median in a list, sorting it
    '''

    # Get the slice of interest
    if start + size > len(Arr):
        size = len(Arr) - start

    myList = Arr[start:start+size]

    # Sort the array
    myList.sort()

    # Return the middle element
    return myList[size // 2]

def fastSelect(Arr: List[int], k: int) -> int:
    '''
    Find the k_th smallest element in the array Arr
    '''

    n = len(Arr)

    # Base check
    if (k > 0 and k <= n):

        medians = []
        arr_less_p = []
        arr_equal_p = []
        arr_more_p = []
        i = 0

        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median, add it to the medians
        #while (i < n // 5):
        while (i < n):
            median = findMedian(Arr, i, 5)
            medians.append(median)
            i += 5

        # Step 3 - Find the median of medians
        if (len(medians) == 1):
            pivot = medians[0]
        elif (len(medians) > 1):
            pivot = fastSelect(medians, (len(medians)//2))

        # Step 4 - Partition the original Arr into three sub-arrays
        for element in Arr:
            if (element<pivot):
                arr_less_p.append(element)
            elif (element>pivot):
                arr_more_p.append(element)
            else:
                arr_equal_p.append(element)

        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if (k <= len(arr_less_p)):
            return fastSelect(arr_less_p, k)

        elif (k > (len(arr_less_p) + len(arr_equal_p))):
            return fastSelect(arr_more_p, (k - len(arr_less_p) - len(arr_equal_p)))

        else:
            return pivot

# Test cases
print('Testing Kth Largest Element solution')

# Test 1
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print('  Test 1: ' + 'Pass' if fastSelect(Arr, k) == 12 else 'Fail' )

# Test 2
Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print('  Test 2: ' + 'Pass' if fastSelect(Arr, k) == 11 else 'Fail' )

# Test 3
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print('  Test 3: ' + 'Pass' if fastSelect(Arr, k) == 99 else 'Fail' )
