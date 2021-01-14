from random import randint
from timeit import repeat

from random import randint

def quick_sort(array):
    
    # Base cases
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select the pivot randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements smaller than the pivot go to the low list
        if item < pivot:
            low.append(item)
        # Elements equal to pivot go to the same list.
        elif item == pivot:
            same.append(item)
        # Elements larger than pivot go to the high list. 
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted low, same, sorted
    return quick_sort(low) + same + quick_sort(high)

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

    check_performance("quick_sort")