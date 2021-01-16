class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):

        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        
        # Base cases
        if self.size() == 0:
            return None

        # Remove the top element placing the last one at the root
        self.next_index -= 1
        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]
        self.cbt[0] = last_element

        # We heapify
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index 

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        """
        We move the last inserted element up until we need.
        """

        child_index = self.next_index

        while child_index >= 1:
        
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            # If we need it, we swap the element with it's parent
            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element
                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        
        parent_index = 0

        while parent_index < self.next_index:

            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            # compare with right child
            if right_child is not None:
                min_element = min(right_child, min_element)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]


# Test cases
heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('  Inserted elements: ' + f'Pass' if elements == [1, 2, 3, 4, 1, 2] else f'Fail ({elements})' )
print('       Size of heap: ' + f'Pass' if heap.size() == 6 else f'Fail ({heap.size()})' )

for i in range(4):
    elem = heap.remove()
    print('        Call remove: ' + f'Pass' if elem == sorted(elements)[i] else f'Fail ({elem})' )

print('   Call get_minimum: ' + f'Pass' if heap.get_minimum() == 3 else f'Fail ({heap.get_minimum()})' )

for i in range(2):
    elem = heap.remove()
    print('        Call remove: ' + f'Pass' if elem == sorted(elements)[i + 4] else f'Fail ({elem})' )

print('       Size of heap: ' + f'Pass' if heap.size() == 0 else f'Fail ({heap.size()})' )
elem = heap.remove()
print('        Call remove: ' + f'Pass' if elem == None else f'Fail ({elem})' )
print('      Call is_empty: ' + f'Pass' if heap.is_empty() else f'Fail ({heap.is_empty()})' )
