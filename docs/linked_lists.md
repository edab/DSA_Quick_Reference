# Linked lists

In a **linked list** the _order_ of the elements is important, since every element contain a reference to the next one, it is possible to have _duplicates_ and the number of elements contained is not fixed.

As opposed to an array, it is fairly simple to add or remove an element, and as an array, searching involve the traverse of all the elements.

There can be essentially three different types of linked lists:

- **Singly Linked Lists**: where every element contain a reference to the next one.
- **Double Linked Lists**: where every element contain a reference to the next and previous one.
- **Circular Linked Lists**: where the chain of nodes link to itself at some point creating a circle.

## Complexity

The _time complexity_ of this data structure, if `K` is the number of element already present would be $O(K)$ for searching an element, and $O(1)$ for inserting an element on the head or on the tail. For _space complexity_, if $N$ is the total number of nodes and $M$ is the size of the data contained into a node will be $O(N * M)$.

## Practice question

## Implementations

### Singly Linked Lists

```python
class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, value):
    if self.head is None:
      self.head = Node(value)
      return
    # Move to the tail (the last node)
    node = self.head
    while node.next:
      node = node.next
    node.next = Node(value)
    return
```

### Double Linked Lists

```python
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
```
