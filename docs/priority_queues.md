# Priority queues

A **Priority queue** is an extension of _queue_, so is a linear _collection_ of elements that support only two types of operation: add elements on one end, and to watch or take the element on the other end, and also have the following properties:

- Every element has a priority associated with it.
- An element with a high priority is dequeued always before one with a low priority.
- Two element with the same priority are dequeued with the same order of insertion.

## Implementation

### Using Heaps

```python
import heapq

customers = []

heapq.heappush(customers, (4, "Star Wars Episode I: The Phantom Menace"))
heapq.heappush(customers, (5, "Star Wars Episode II: Attack of the Clones"))
heapq.heappush(customers, (6, "Star Wars Episode III: Revenge of the Sith"))
heapq.heappush(customers, (1, "Star Wars Episode IV: A New Hope"))
heapq.heappush(customers, (2, "Star Wars Episode V: The Empire Strikes Back"))
heapq.heappush(customers, (3, "Star Wars Episode VI: Return of the Jedi"))

while customers:
     print(heapq.heappop(q))

# Will print first star wars films in chronological order.
```

### Using queue.PriorityQueue

```python
from queue import PriorityQueue

pqueue = PriorityQueue()

pqueue.put(customers, (4, "Star Wars Episode I: The Phantom Menace"))
pqueue.put(customers, (5, "Star Wars Episode II: Attack of the Clones"))
pqueue.put(customers, (6, "Star Wars Episode III: Revenge of the Sith"))
pqueue.put(customers, (1, "Star Wars Episode IV: A New Hope"))
pqueue.put(customers, (2, "Star Wars Episode V: The Empire Strikes Back"))
pqueue.put(customers, (3, "Star Wars Episode VI: Return of the Jedi"))

while customers:
     print(customers.get())

# Will print first star wars films in chronological order.
```
