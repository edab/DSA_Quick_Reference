#  Maximum Subarray Problem

The **Maximum Subarray Problem** is another problem that can illustrate the _Divide and Conquer_ technique, and is defined as:

> Given an unsorted list `A=[a_1, a_2, ..., a_n]` of n integers, find the maximum sum of contiguous elements among all the possible subarrays.

The first _brute force_ solution, that iterate two indices between 0 and n, and for each pair compute the sum for a third loop, will have a complexity of $O(n^3)$.

```python
for i in rage(n):
    for j in range(i,n):
        sum = 0
        for k in range(i,j):
            sum += arr[k];
        if (sum > max)
            max = sum;
```

The second _brute force_ solution, that for each element, calculate the sum of all other elements, will have a complexity of $O(n^2)$.

```python
for i in rage(n):
    sum = 0
    for j in range(i,n):
        sum += arr[j];
        if (sum > max)
            max = sum;
```

The _divide and conquer_ solution, should follow the usual template of this types of algorithms:

- Define a _Base Case_.
- Split the problem into subproblems using recursion and solve them.
- Merge the solutions.

## Implementation

Python3 implementation: [dac_maximum_subarray.py](../solutions/dac_maximum_subarray.py)

One possible implementation that use the _divide and conquer_ approach can be:

- if `n == 1` simply return the element (base case).
- Otherwise split the array in three parts and calculate the sums obtaining:
  - `left_sum`: the sum of the left subarray containing $n/2$ elements.
  - `cross_sum`: the sum of subarray containing both left and right subarrays.
  - `rigth_sum`: the sum of the right subarray containing $n/2$ elements.
- Merge the subproblems solutions with max(left_sum, right_sum, cross_sum)

```
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
```
