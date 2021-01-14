# Quick sort

The **Quick sort** is another sorting algorithm based on the divide and conquer approach. The algorithm first selects a **pivot** element, and then divide, or partition, the input array into two lists around the pivot, the first with small items and the second with large items.

The algorithm then sorts both lists recursively until the resultant list is completely sorted.

The pivot help dividing the two list with elements that differs, making more efficient each recursive iteration. The pivot selection affect the performance of the algorithm.

## Complexity

With _Quick sort_, the input list is partitioned in linear time, $O(N)$, and this process repeats recursively an average of $O(log_2 N)$ times. This leads to a final complexity of $O(N log_2N)$.

By using the median value as the pivot, you end up with a final runtime of O(n) + O(n log2n). You can simplify this down to O(n log2n) because the logarithmic portion grows much faster than the linear portion.

## Implementation

Python3 implementation: [quick_sort.py](../solutions/quick_sort.py)

Although its worst-case scenario is theoretically $O(N^2)$, in practice, a good implementation of quicksort beats most other sorting implementations, and just like merge sort, is straightforward to parallelize.

One of the main disadvantages is the lack of a guarantee that it will achieve the average runtime complexity.

_Quick sort_ also trades off memory space for speed. This may become a limitation for sorting larger lists.

```python

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

```
