# Median Problem

The **Median Problem** can be a perfect example for the divide and conquer solving technique, and is defined as:

> Given an unsorted list `A=[a_1, a_2, ..., a_n]` of n positive integers, found the median of A.

We define a _median_ element as the $[n/2]^{th}$ element of the sorted list, and we focus on the solution a more general problem, to find the $k^{th}$ element, where `k` is a number between 1 and n.

The first solution could be to first sort the algorithm, and then directly get the $k^{th}$ element. Since there is a sort operation, the total runtime of this solution would be in order of $O(n\ log\ n)$.

But there is a better solution, know as [Median of medians](http://people.csail.mit.edu/rivest/pubs/BFPRT73.pdf), thanks to Blum, Floyd, Pratt,. Rivest, Tarjan (1973).

The solution architecture remind the _Quicksort_ algorithm, that works as follow:

1. We choose a _pivot_ `p`.
2. We move all the array element into three bucket, `A<p`, `A=p`, `A>p`.
3. The algorithm is recursively applied to `A<p` and the `A>p`.
4. The final output will be the sorted list of `A<p`, then the `A=p` element and `A>p`.

If we chose the wrong _pivot_, like the maximum or minimum element, the time complexity of the quicksort will be $O(N^2)$.

The _perfect pivot_ would be the median of A, but since is the ones we are searching for, we target a _good pivot_, that appears in the region from 1/4 to 3/4 of the sorted array A.

## Implementation

Python3 implementation: [kth_largest_element_dac.py](../solutions/problems/kth_largest_element_dac.py)

A nice solution to the problem can be:
1. Break A in 5 groups of $n/5$ elements each (one swipe of the array, $O(N)$).
2. For each group, sort the group and find the median of each group (only sort 5 element, $O(1)$ for each group, $O(N)$).
3. Create a list S of median of all groups.
4. Run the same first three steps on array S of length $n/5$ ($O(N/5)$).
5. Partition the array A into three bucket, $A<p$, $A=p$, $A>p$ (one swipe of the array, $O(N)$).
6. Recourse on $A<p$, $A>p$ or output p depending on k value ($O(3n/4)$, since p is a good pivot, and the two bucket have a maximum size of $3n/4$).

So, with this algorithm, we have a time complexity of $O(N)$, that is a great improvement over the one of the simple solution of sorting first, and the select the key.
