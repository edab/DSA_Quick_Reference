# Divide and Conquer

A **Divide and Conquer** algorithm use recursion for break down a problem into subproblems until they become easy enough to be solved directly. The solution of the subproblems has to be then combined in some way for obtaining the final result.

Examples of _divide-and-conquer_ algorithms are very efficient solution to a variety of problems like: sorting (merge-sort, quicksort), multiply large numbers (Karatsuba algorithm), closest pair problem, syntactic analysis, discrete Fourier transform computation, matrix multiplication (Strassen algorithm).

The main advantages of this technique are:

- Ability to solve complex problem.
- Obtain efficient algorithms.
- Ability to be run on parallel architectures.
- Efficient uses of cache, since the subproblems are small.

The use of _recursion_ make the code harder to debug and requires large stacks, and in some cases the stack used is limited. Non recursive implementation should use alternatives data structures.
