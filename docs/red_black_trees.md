# Red Black Tree

A **Red Black Tree** is a type of _self-balanced binary search tree_, where each node has an additional color attribute that can be Red or Black, useful for checking if the tree continue to be balanced after inserting and removing elements from the data structure.

In addition to the requirements of a generic _binary search tree_, the following rules should also be applied:

- Each node is either **Black** or **Red**
- The **root node** is _Black_.
- Leaf nodes have NULL children, all _Black_.
- If a node is _Red_, then both children are _Black_.
- Every path from a given node to a NULL descendant goes through the same number of _Black_ nodes.

## Complexity

The _time complexity_ in this data structure, if `N` is the number of element already present, is $O(log\ N)$ for search, insert or delete elements, and the _space complexity_ is $O(N)$.
