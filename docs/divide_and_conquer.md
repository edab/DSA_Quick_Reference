# Divide and Conquer

A **Divide and Conquer** algorithm use recursion for break down a problem into subproblems until they become easy enough to be solved directly. The solution of the subproblems has to be then combined in some way for obtaining the final result.

Examples of _divide-and-conquer_ algorithms are very efficient solution to a variety of problems like: sorting (merge-sort, quicksort), multiply large numbers (Karatsuba algorithm), closest pair problem, syntactic analysis, discrete Fourier transform computation, matrix multiplication (Strassen algorithm).

The main advantages of this technique are:

- Ability to solve complex problem.
- Obtain efficient algorithms.
- Ability to be run on parallel architectures.
- Efficient uses of cache, since the subproblems are small.

The use of _recursion_ make the code harder to debug and requires large stacks, and in some cases the stack used is limited. Non recursive implementation should use alternatives data structures.

## Median Problem

Python3 implementation: [dac_kth_largest_element.py](../solutions/dac_kth_largest_element.py)

The _Median Problem_ can be a perfect example for this solving technique, and can be defined as: given an unsorted list `A=[a_1, a_2, ..., a_n]` of n elements, found the median of A.

We define a _median_ element as the $[n/2]^{th}$ element of the list, and we focus on the solution a more general problem, to find the $k^{th}$ element, where `k` is a number between 1 and n.

The first solution could be to first sort the algorithm, and then directly get the $k^{th}$ element. Since there is a sort operation, the total runtime of this solution would be in order of $O(n\ log\ n)$.

But there is a better solution, know as [Median of medians](http://people.csail.mit.edu/rivest/pubs/BFPRT73.pdf), thanks to Blum, Floyd, Pratt,. Rivest, Tarjan (1973).

The solution architecture remind the _Quicksort_ algorithm, that works as follow:

1. We choose a _pivot_ `p`.
2. We move all the array element into three bucket, `A<p`, `A=p`, `A>p`.
3. The algorithm is recursively applied to `A<p` and the `A>p`.
4. The final output will be the sorted list of `A<p`, then the `A=p` element and `A>p`.

If we chose the wrong _pivot_, like the maximum or minimum element, the time complexity of the quicksort will be $O(N^2)$.

The _perfect pivot_ would be the median of A, but since is the ones we are searching for, we target a _good pivot_, that appears in the region from 1/4 to 3/4 of the sorted array A.

### Fast median solution

A nice solution to the problem can be:
1. Break A in 5 groups of $n/5$ elements each (one swipe of the array, $O(N)$).
2. For each group, sort the group and find the median of each group (only sort 5 element, $O(1)$ for each group, $O(N)$).
3. Create a list S of median of all groups.
4. Run the same first three steps on array S of length $n/5$ ($O(N/5)$).
5. Partition the array A into three bucket, $A<p$, $A=p$, $A>p$ (one swipe of the array, $O(N)$).
6. Recourse on $A<p$, $A>p$ or output p depending on k value ($O(3n/4)$, since p is a good pivot, and the two bucket have a maximum size of $3n/4$).

So, with this algorithm, we have a time complexity of $O(N)$, that is a great improvement over the one of the simple solution of sorting first, and the select the key.
