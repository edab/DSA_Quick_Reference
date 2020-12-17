# Deques

A **Deque** is a linear _collection_ of elements that support four types of operation: add and remove an elements on one end, and add and remove an element on the other end.

You can't get the element on the center, you need to remove all the other element from one of the two sides to reach it.

A deque is a generalized version of both _stacks_ and _queue_, and is natively implemented in python 3.

## Terminology

There is some specific terminology associated with the queue:

- `Head`: the first and oldest element in the queue.
- `Tail`: the last and newest element in the queue.
- `Enqueue`: add an element to the queue.
- `Dequeue`: remove an element from the queue.
- `Peek`: read, but not remove, the most recent element.

## Complexity

The _time complexity_, if `N` is the number of element already present, will be $O(1)$ for both `enqueue` and `dequeue`, and $O(N)$ for `access` or `search` operations.

For _space complexity_, if $N$ is the total number of nodes and $M$ is the size of the data contained into a node will be $O(N * M)$.

## Implementations

Python has and implementation of deque.

```python
from collection import deque

# make a new deque with three items
d = deque('ghi')                 

# iterate over the deque's elements
for elem in d:                   
  print(elem.upper())

# The right side use common names for methods, the left side add "left" trailer
d.append('j')          # add a new entry to the right side
d.appendleft('f')      # add a new entry to the left side ['f', 'g', 'h', 'i', 'j']

d.pop()                # return and remove the rightmost item ('j')
d.popleft()            # return and remove the leftmost item ('f')
list(d)                # list the contents of the deque ['g', 'h', 'i']
d[0]                   # peek at leftmost item ('g')
d[-1]                  # peek at rightmost item ('i')

list(reversed(d))      # list the contents of a deque in reverse ['i', 'h', 'g']
'h' in d               # search the deque (True)
d.extend('jkl')        # add multiple elements at once
print(d)               # -> ['g', 'h', 'i', 'j', 'k', 'l']
d.rotate(1)            # right rotation ['l', 'g', 'h', 'i', 'j', 'k']
d.rotate(-1)           # left rotation ['g', 'h', 'i', 'j', 'k', 'l']

d.clear()              # empty the deque

d.extendleft('abc')    # extendleft() reverses the input order ['c', 'b', 'a']

```
