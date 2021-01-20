# Red Black Tree

A **Red Black Tree** is a type of _self-balanced binary search tree_, where each node has an additional color attribute that can be Red or Black, useful for keeping the tree balanced.

A _self-balanced tree_ is a type of tree that tries to minimize the number of levels used and does some operations during the insertions and deletions of nodes to maintain this property.

In addition to the requirements of a generic _binary search tree_, the following rules should also be applied:

- Each node has a color, either **Black** or **Red**
- Every node has a children, or a NULL leaf node.
- All NULL leaf nodes are _Black_.
- If a node is _Red_, then both children must be _Black_.
- The **root node** is _Black_ (optional rule).
- Every path from to a node descendant must contain the same number of _Black_ nodes.

## Complexity

The _time complexity_ in this data structure, if `N` is the number of element already present, is $O(log\ N)$ for search, insert or delete elements, and the _space complexity_ is $O(N)$.

## Operations

### Insert

The new node insertion, usually a _Red_ node, require different actions, depending on the state of the tree:

1. ***Insert the Root Node***: if we adhere to the _Black_ root node rule, we need to change the color, and add two NULL children.
2. ***Insert the node at a Black Parent***: we need only to add two NULL children.
3. ***Parent and Sibling are both Red***: we switch the parent and sibling color to _Black_, and the grand parent color to _Red_. We should also check all the other nodes, to see if we violated some rule now for other nodes.
4. ***Parent is Red and Sibling is NULL Black***: we need to perform a rotation. If the node is a right child, and the parent is a left child, we perform a CCW rotation.
5. ***Parent and Child are both Red and on the same side of their parent***: we perform
a right rotation and change the children colors.

## Implementations

Python3 implementation: [red_black_tree.py](../solutions/red_black_tree.py)

### Node

Other than the new color attribute, we should have also a reference to the parent, so we can easily check if the parent node is _Red_ or _Black_, and do rotation.

```python
class Node(object):
  def __init__(self, value, parent, color):
    self.value = value
    self.left = None
    self.right = None
    self.parent = parent
    self.color = color
```

### Tree

The _Red Black Tree_ implementation need different helper function for work:

- `grandparent()`: used for get the parent of a parent of a node.
- `pibling()`: used for getting the node's parent's sibling.
- `insert_helper()`: for insert in the right place the node using recursion.
- `rebalance()`: for rebalancing the tree after the insertion and removing of a node.

```python

class RedBlackTree(object):

  def __init__(self, root):
    self.root = Node(root, None, 'red')

  def insert(self, new_val):
    new_node = self.insert_helper(self.root, new_val)
    self.rebalance(new_node)

  def insert_helper(self, current, new_val):
    if current.value < new_val:
      if current.right:
        return self.insert_helper(current.right, new_val)
      else:
        current.right = Node(new_val, current, 'red')
        return current.right
    else:
      if current.left:
        return self.insert_helper(current.left, new_val)
      else:
        current.left = Node(new_val, current, 'red')
        return current.left

  def rebalance(self, node):

    # Case 1: Insert the Root Node
    if node.parent == None:
      return

    # Case 2: Insert the node at a Black Parent
    if node.parent.color == 'black':
      return

    # Case 3: Parent and Sibling are both Red
    if self._pibling(node) and self._pibling(node).color == 'red':
      self._pibling(node).color = 'black'
      node.parent.color = 'black'
      self._grandparent(node).color = 'red'
      return self.rebalance(self._grandparent(node))

    # If there is no gp, we have done
    gp = self._grandparent(node)
    if gp == None:
      return

    # Case 4: Parent is Red and Sibling is NULL Black
    if gp.left and node == gp.left.right:
      self.rotate_left(node.parent)
      node = node.left
    elif gp.right and node == gp.right.left:
      self.rotate_right(node.parent)
      node = node.right

    # Case 5: Parent and Child are both Red and on the same side of
    #         their parent
    p = node.parent
    gp = p.parent
    if node == p.left:
      self.rotate_right(gp)
    else:
      self.rotate_left(gp)
    p.color = 'black'
    gp.color = 'red'

  def search(self, find_val):
    return False

```
