# Bubble sort

The **Bubble Sort** algorithm take his name from the way the algorithm works: at every new pass, the largest element in the list “bubbles up” toward its correct position.

The main advantage of the bubble sort algorithm is its simplicity, and the disadvantage is that it is slow.

## Complexity

The bubble sort consists of two nested for loops, that performs $n - 1$ comparisons the first iteration, $n - 2$ comparisons the second iteration, and so on until the final comparison is done.

This comes at a total of $(n - 1) + (n - 2) + (n - 3) + … + 2 + 1 = n (n-1) / 2$ comparisons, which lead to a $O(N^2)$ time complexity.

## Implementation

Python3 implementation: [bubble_sort.py](../solutions/bubble_sort.py)

We can implement two optimizations in this algorithm. We can check at each iteration if the list is already sorted, and in case we return the list. We can also compare at each cycle one less element, since the preceding iteration already move it on the right position.

```python

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
```
