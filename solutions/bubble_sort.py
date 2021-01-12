from random import randint
from timeit import repeat
 
def bubble_sort(array):

    N = len(array)

    for i in range(N):

        # Check if the array is already sorted
        already_sorted = True

        # At each iteration we shorten the interval already sorted
        for j in range(N - i - 1):

            if array[j] > array[j + 1]:

                # Swap the items
                array[j], array[j + 1] = array[j + 1], array[j]

                # We are not sure the `already_sorted` is sorted
                already_sorted = False

        # If there were no swaps, we can terminate
        if already_sorted:
            break

    return array

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

    check_performance("bubble_sort")
