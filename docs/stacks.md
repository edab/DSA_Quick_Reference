# Stacks

A **Stack** or **LIFO** (Last In First Out), is a linear _collection_ of elements that support only two type of operations: add elements on the _top_, and watch or remove the most recent element present on the _top_.

It is not possible to get the element on the bottom, since you need to make your way through everything above it to reach it, removing elements one by one.

Stacks are extremely useful when you only care about the _most recent element_, or when the _order_ in which you see and add elements actually matters.

Since the stack definition is quite open, we can implement them in different ways:

- using _linked lists_, keeping track of the head (or tail) where you always insert the last recent element.
- using _arrays_, where we need to address the problem of allocating more space when needed.
- using _python 3_ internal list implementation.

## Terminology

The typical operations defined for the stacks have a specific terminology:

- `Push`: used for inserting a new element on the top.
- `Pop`: used for removing the most recent element.
- `Peek`: used for read, but not remove, the most recent element.

## Complexity

The _time complexity_, if `N` is the number of element already present, will be $O(1)$ for both `pop` and `push`, and $O(N)$ for `access` or `search` operations.

For _space complexity_, if $N$ is the total number of nodes and $M$ is the size of the data contained into a node will be $O(N * M)$.

## Practice question

- **Balanced Parentheses**: given an input string that contain parentheses, like in mathematical expressions, return True if they are balanced.
- **Reverse Polish notation**: given a reverse polish expression as input, evaluate and return the correct final answer.
- **Reverse a stack**
- **Minimum bracket reversals**: given an input string consisting of only `{` and `}`, figure out the minimum number of reversals required to make the brackets balanced.

## Implementations

### Using dynamic arrays

Python3 implementation: [stack_using_array.py](../solutions/stack_using_array.py)

If we use an array, we should allocate some space at the beginning, and then when is needed more we need to allocate another array with doubled size, and copy all existent element there.

```python
class Stack:

  def __init__(self, initial_size = 10):
    self.arr = [0 for _ in range(initial_size)]
    self.next_index = 0
    self.num_elements = 0

  def push(self, data):
    if self.next_index == len(self.arr):
      print("Out of space! Increasing array capacity ...")
      self._handle_stack_capacity_full()
    self.arr[self.next_index] = data
    self.next_index += 1
    self.num_elements += 1

  def peek(self):
    if self.is_empty():
      return None
    return self.arr[self.next_index - 1]

  def pop(self):
    if self.is_empty():
      self.next_index = 0
      return None
    self.next_index -= 1
    self.num_elements -= 1
    return self.arr[self.next_index]

  def size(self):
    return self.num_elements

  def is_empty(self):
    return self.num_elements == 0

  def _handle_stack_capacity_full(self):
    old_arr = self.arr
    self.arr = [0 for _ in range( 2* len(old_arr))]
    for index, element in enumerate(old_arr):
      self.arr[index] = element
```

### Using linked lists

Python3 implementation: [stack_using_linked_list.py](../solutions/stack_using_linked_list.py)

```python
class Node:

  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:

  def __init__(self):
    self.head = None
    self.num_elements = 0

  def push(self, value):
    new_node = Node(value)

    if self.head:
      new_node.next = self.head

    self.head = new_node

    self.num_elements += 1

  def peek(self):
    if self.is_empty():
      return None
    return self.head.value

  def pop(self):
    if self.is_empty():
      return

    value = self.head.value
    self.head = self.head.next

    return value

  def size(self):
    return self.num_elements

  def is_empty(self):
    return self.num_elements == 0
```

# Using Python 3 list

Python3 implementation: [stack_using_python_list.py](../solutions/stack_using_python_list.py)

```python
class Stack:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()
```
