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

# Test case
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print ("Pass" if (q.size() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 1) else "Fail")
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
