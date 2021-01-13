from random import randint
from timeit import repeat

def merge(left, right):

    # Base cases
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Until the output array is complete
    while len(result) < len(left) + len(right):

        # We next result element is taken from the smaller between left or right
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, we can directly add the remaining one
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):

    # Base cases
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input into two equal halves
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

# Tests cases

# Performance evaluation
def check_performance(algorithm):

    ARRAY_LENGTH = 1000

    # Generate an array of `ARRAY_LENGTH` random integer between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Execute the code ten times and return the time that each execution took
    stmt = f"{algorithm}({array})"
    setup_code = f"from __main__ import {algorithm}"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Display the name of the algorithm and the minimum time it took to run
    print(f"Algorithm: {algorithm}, minimum execution time: {min(times)}")


if __name__ == "__main__":

    check_performance("merge_sort")