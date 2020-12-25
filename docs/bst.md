# Binary Search Tree

A **Binary Search Tree** or **BST**, is a special type of binary tree, an _ordered binary tree_. All the nodes in the left sub-tree are less than or equal to the value of the node, and all the node in the right sub-tree are greater than the value of the node.

<img src='https://g.gravizo.com/svg?
  digraph G {
    5 -> 3 -> 1;
    3 -> 4;
    5 -> 7 -> 9;
    7 -> 10;
  }
'/>

_BST_ allows fast lookup, addition and removal of data items, and can be used to build _dynamic sets_ and _lookup tables_.

## Complexity

The order of the _BST_ means that each comparison skips about half of the remaining tree, so the whole lookup takes time proportional to the binary logarithm of the number of items stored in the tree.

Algorithm | Average | Worst case
:-- | :-- | :--
Space  | $O(n)$     | $O(n)$
Search | $O(log\ n)$ | $O(n)$
Insert | $O(log\ n)$ | $O(n)$
Delete | $O(log\ n)$ | $O(n)$

## Implementation

Since a _BST_ is a binary tree, we first create a node with left and right children.

```python
class Node:

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
```

A _BST_ is essentially made by a root node, and the structure makes looking for the node with the maximum and minimum values very easy, we just need to traverse to the leftmost (minimum) or rightmost node:

```python
class Tree():

    def __init__(self):
        self.root = None

    def find_min(self):
        node = self.root
        while node.left_child:
            node = node.left_child
        return node.value

    def find_max(self):
        node = self.root
        while node.right_child:
            node = node.right_child
        return node.value
```

In a _BST_ the nodes must be inserted in a specific way. We first need to compare the new value with the current node.

In case is less than the current node value, we move the the left child, otherwise we move to its right child.

In case the node is not existent, we can create a new node with the value and insert it in that place.

```python
    def insert(self, new_value):

        new_node = Node(new_value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            parent = None

            while True:
                parent = current
                if new_node.value < current.value:
                    current = current.left_child
                    if current is None:
                        parent.left_child = new_node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = new_node
                        return
```

The delete operation is more complex, because we need to consider different scenarios, related to the status of the node that we want to remove:

- The node has no children: in this case we just need to detach to its parent.
- The node has one child: in this case we need to preserve the relationship between its parent and its child. We need to remove the node, and connect its child to its parent.
- The node has two children: this is the most complex scenario. We need to find the next biggest descendant of node to remove, also called the in-order successor. Then we replace the value of the node to remove with the one of the in-order successor, and the we remove the in-order successor. In removing that node, we apply again the same rules here described, in case it has no, one or two children.

```python
    def delete(self, value):

         curr = self.root
         prev = None

         # Safe check, the value is actually present in the BST?
         while(curr != None and curr.value != value):
             prev = curr
             if curr.value < value:
                 curr = curr.right_child
             else:
                 curr = curr.left_child

         # If the value is not found, there is nothing to delete
         if curr == None:
             return

         # Check if the node to be deleted has at most one child
         if curr.left_child == None or curr.right_child == None:

             # newCurr will replace the node to be deleted
             newCurr = None

             # if the left child does not exist.
             if curr.left_child == None:
                 newCurr = curr.right_child
             else:
                 newCurr = curr.left_child

             # check if the node to be deleted is the root.
             if prev == None:
                 return newCurr

             # Check if the node to be deleted is prev's left or right child and
             # then replace this with newCurr
             if curr == prev.left_child:
                 prev.left_child = newCurr
             else:
                 prev.right_child = newCurr

             curr = None

         # node to be deleted has two children.
         else:

             p = None
             temp = None

             # Compute the inorder successor of curr.
             temp = curr.right_child
             while(temp.left_child != None):
                 p = temp
                 temp = temp.left

             # check if the parent of the inorder successor is the root or not.
             # if it isn't, then make the left child of its parent equal to the
             # inorder successor's right child.
             if p != None:
                 p.left = temp.right

             else:

                 # if the inorder successor was the root, then make the right
                 # child of the node to be deleted equal to the right child of
                 # the inorder successor.
                 curr.right_child = temp.right_child

             curr.value = temp.value
             temp = None
```
