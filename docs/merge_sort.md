# Merge sort

The **Merge sort** is a very efficient sorting algorithm, based on the divide and conquer approach. This algorithms have the follow structure:

- The original input is broken into several parts, each one representing a subproblem that’s similar to the original but simpler.
- Each subproblem is solved recursively.
- The solutions to all the subproblems are combined into a single overall solution.

## Complexity

To analyze the complexity of merge sort, given N as the length of the original input array, we can look at its two steps separately:

- The _basic merge() function_ has a linear runtime $O(N)$, since it receives two arrays whose combined length is at most N, and it merge them by looking at each element at most once.

- The _recursive main function_ splits the input array recursively and calls _merge()_ for each half. Since the array is halved until a single element remains, the total number of halving operations performed by this function is $log_2N$.

Since _merge()_ is called for each half, we get a total runtime of $O(n \ log_2N)$.

## Implementation

Python3 implementation: [merge_sort.py](../solutions/merge_sort.py)

The implementation of the _Merge Sort algorithm_ needs two different functions:

- A function that recursively splits the input in half
- A function that merges both halves, producing a sorted array

```python

def merge(left, right):

    # Base cases
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Until the resulting array is complete
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

```
