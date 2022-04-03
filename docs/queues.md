# Queues

A **Queue** or **FIFO** (First In First Out), is a linear _collection_ of elements that support only two types of operation: add elements on one end, and to watch or take the element on the other end.

You can't get the element on the center, you need to remove all the other element to reach it.

Since the queue definition is quite open, we can implement them in different ways:

- using _linked lists_, keeping track of the head (or tail) where you always insert the last recent element.
- using _arrays_, where we need to address the problem of allocating more space when needed.
- using _Python_ internal list implementation.
- using _Python_ internal deque data structure (implemented in python as a doubly linked list).

## Terminology

There is some specific terminology associated with the queue:

- `Head`: the first and oldest element in the queue.
- `Tail`: the last and newest element in the queue.
- `Enqueue`: add an element to the queue.
- `Dequeue`: remove an element from the queue.
- `Peek`: read, but not remove, the most recent element.

## Complexity

### Time complexity

| Operation | List based | Deque based
| :-- | :-- | :--
| Pop/Append items on the right end (Enqueue) | _O(1)_ + reallocation | _O(1)_
| Pop/Append items on the left end (Dequeue) | _O(N)_ | _O(1)_
| Accessing arbitrary items through indexing | _O(1)_ | _O(N)_
| Inserting and deleting items in the middle | _O(N)_ | _O(N)_
| Search | _O(N)_ | _O(N)_

The _space complexity_ is _O(N)_, where _N_ is the total number of elements present in the queue.

## Practice question

- **Reverse a queue**
- **Implement a queue using stacks**

## Implementations

### Using dynamic arrays

Python3 implementation: [queue_using_array.py](../solutions/queue_using_array.py)

```python
class Queue:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()

        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        if self.is_empty():
            self.front_index = -1
            self.next_index = 0
            return None

        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def __len__(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]
        index = 0

        # copy all elements from front of queue (front-index) until end
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # case: when front-index is ahead of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        self.front_index = 0
        self.next_index = index
```

### Using linked lists

Python3 implementation: [queue_using_linked_list.py](../solutions/queue_using_linked_list.py)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def __len__(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
```

### Using Python 3 list

Python3 implementation: [queue_using_python_list.py](../solutions/queue_using_python_list.py)

```python
class Queue:

    def __init__(self):
        self._storage = list()

    def __len__(self):
        return len(self._storage)

    def __contains__(self, item):
        return item in self._storage

    def __iter__(self):
        yield from self._storage

    def __repr__(self):
        return f"Queue({list(self._storage)})"

    def enqueue(self, item):
        self._storage.append(item)

    def dequeue(self):
        try:
            return self._storage.pop()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None

```

### Using Python Deque

```Python
from collections import deque

class Queue:

    def __init__(self):
        self._storage = deque()

    def __len__(self):
        return len(self._storage)

    def __contains__(self, item):
        return item in self._storage

    def __iter__(self):
        yield from self._storage

    def __repr__(self):
        return f"Queue({list(self._storage)})"

    def enqueue(self, item):
        self._storage.append(item)

    def dequeue(self):
        try:
            return self._storage.popleft()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None

```
