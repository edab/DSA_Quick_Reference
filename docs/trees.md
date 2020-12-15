# Trees

A **Tree** is a non linear _collection_ of elements called nodes connected by edges. There cannot be cycles or unconnected nodes, that support four types of operation: add and remove an elements on one end, and add and remove an element on the other end.

## Terminology

There is some specific terminology associated with the tree:

- `Level` of a node: number of edges to the root plus one.
- `Parent`: node connected to a higher level.
- `Child`: node connected to a lower level.
- `Leaf`: node that has no children.
- `Edge`: connection between two nodes.
- `Path`: group of connections.
- `Height` of a node: number of level between it and the further leaf of the tree.
- `Depth` of a node: number of edges to the root.

## Operations

### Insert

Inserting an element into a _Tree_ when he has no order is a simple operation, all we need to do is find the first node that doesn't have all the children and add to it the new node. In the worst case is that we travel the longest path until we found the leaf.

### Delete

###

### Traversal

Since a _Tree_ is a not linear data structure, can be traversed in multiple ways.

![tree](../images/tree.png)

There are two common approach used to explore it:

- **Depth First Search (DFS)**: were the priority is to explore child nodes first. There are three main way to do this.
  - **pre-order**: visit a node, traverse it's left subtree and then it's right subtree [D, B, A, C, E, F]
  - **in-order**: traverse it's left subtree, visit the node, traverse it's right subtree [A, B, C, D, E, F]
  - **post-order**: traverse it's left subtree, traverse it's right subtree and then visit the node. [A, C, B, F, E, D]
- **Breath First Search (BFS)**: were the priority is to visit each node that has the same level, before visiting child nodes. [D, B, E, A, C, F]

## Implementation

### Basic Binary Tree

Python3 implementation: [binary_tree.py](../solutions/binary_tree.py)

```python
class Node:

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class Tree:

    def __init__(self,value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root
```

### Depth First Search

#### Pre Order

This is the iterative version.

```python
def pre_order_iterative(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()

    if node == None:
        return []

    stack.push(node)

    while(not stack.is_empty()):

        node = stack.pop()
        visit_order.append(node.value)

        if node.right_child:
            stack.push(node.right_child)
        if node.left_child:
            stack.push(node.left_child)
```

This is the recursive version.

```python
def pre_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            visit_order.append(node.value)
            traverse(node.left_child)
            traverse(node.right_child)

    traverse(tree.get_root())

    return visit_order
```

#### In Order

This is the iterative version.

```python
def in_order_iterative(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()

    if node == None:
        return []

    while(not stack.is_empty() or node):

        if node:
            stack.push(node)
            node = node.left_child
        else:
            node = stack.pop()
            visit_order.append(node.value)
            node = node.right_child

    return visit_order
```

This is the recursive version.

```python
def in_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            traverse(node.left_child)
            visit_order.append(node.value)
            traverse(node.right_child)

    traverse(tree.get_root())

    return visit_order
```

#### Post Order

This is the iterative version.

```python
def post_order_iterative(tree):
    visit_order = list()
    last_node_visited = None
    stack = Stack()
    node = tree.get_root()

    if node == None:
        return []

    while(not stack.is_empty() or node):

        if node:
            stack.push(node)
            node = node.left_child
        else:
            peek_node = stack.peek()
            if peek_node.right_child and last_node_visited != peek_node.right_child:
                node = peek_node.right_child
            else:
                visit_order.append(peek_node.value)
                last_node_visited = stack.pop()

    return visit_order
```

This is the recursive version.

```python
def post_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            traverse(node.left_child)
            traverse(node.right_child)
            visit_order.append(node.value)

    traverse(tree.get_root())

    return visit_order
```
