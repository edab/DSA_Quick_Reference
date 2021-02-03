 # Heaps

A **heap** is a special _Tree_ based data structures, where element are arranged in increasing or decreasing order, and for this reason there are two types of heaps:

- _Max heap_: where the root node represent the greatest value among all the key present. That rule should also be true among all the other child nodes.
- _Min heap_: where the root node represent the smallest value among all the key present. That rule should also be true among all the other child nodes.

A special type of Heap is a _Binary Heap_, where some additional rules apply:

- Every node can have a maximum of two children.
- All levels should be completely full.
- If the last level isn't full, elements should be added from left to right.

There are many different variants of _Heaps_:

- _Fibonacci heap_: has better amortized running time, discovered by [Fredman and Tarjian](http://bioinfo.ict.ac.cn/~dbu/AlgorithmCourses/Lectures/Fibonacci-Heap-Tarjan.pdf).
- _Brodal queue_: was the first heap variant to achieve $O(1)$ for every operation except for deletion, and was developed by [Gerth Stølting Brodal](http://www.brics.dk/RS/96/37/BRICS-RS-96-37.pdf).

## Operations

### Insert

We add the new element in the next open spot following the heap filling rules (search the last level, and starting from left find a missing element), and then we _heapify_, ensuring that the greatest or smallest node is on top.

### Remove

We remove the last spot moving the key to the one we want to remove, mostly the root spot, and then we _heapify_, ensuring that the greatest or smallest node is on top.

## Complexity

In a _Max Binary Heap_, a function that will read the maximum key would happen in constant time $O(1)$, and the same apply to the _Min Binary Heap_ for the minimum value.

Searching a value doesn't achieve the same result of a Binary Tree, since we cannot know in which direction we will find our value, so it will be a linear operation $O(N)$ in the worst case, but the average case is $O(N/2)$ since if we exclude a node we can exclude it's sub-tree, since the node is the maximum/minimum key of that sub-tree.

Insert and remove operations take $O(log N)$, and involve moving a node to the root swapping with it's parent, with as many operation as the height of the tree.

## Implementation

Often _Heaps_ are represented as an array, since always fill a heap level by level from left to right, saving space.

Python offer also an implementation of _Heaps_ very easy to use.

### Max Binary Heap

Python3 implementation: [heap.py](../solutions/heap.py)

### Python Heap

```
import heapq

H = [21,1,45,78,3,5]

# Covert to a heap
heapq.heapify(H)         # ->    [1, 3, 5, 78, 21, 45]

# Add element
heapq.heappush(H,8)      # ->    [1, 3, 5, 78, 21, 45, 8]

# Remove element from the heap
heapq.heappop(H)         # -> 1, [3, 8, 5, 78, 21, 45]

# Replace an element
heapq.heapreplace(H, 6)  # ->    [5, 8, 6, 78, 21, 45]
```
