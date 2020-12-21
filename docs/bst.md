# Binary Search Tree

A **Binary Search Tree** or **BST**, is an _ordered binary tree_ where every nodes store a key that is greater than all the keys in the node's left subtree, and less than those in its right subtree.

_BST_ allows fast lookup, addition and removal of data items, and can be used to build _dynamic sets_ and _lookup tables_.

## Complexity

The order of the _BST_ means that each comparison skips about half of the remaining tree, so the whole lookup takes time proportional to the binary logarithm of the number of items stored in the tree.

Algorithm | Average | Worst case
:-- | :-- | :--
Space  | $O(n)$     | $O(n)$
Search | $O(log\ n)$ | $O(n)$
Insert | $O(log\ n)$ | $O(n)$
Delete | $O(log\ n)$ | $O(n)$
