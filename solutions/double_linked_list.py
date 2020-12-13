class DoubleNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoubleLinkedList:

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

    def delete(self, value):
        node = self.head
        while node:
            if node.value == value:
                if node == self.head:
                    self.head == node.next
                    self.head.previous = None
                elif node == self.tail:
                    self.tail == node.previous
                    self.tail.next = None 
                else:
                    node.previous.next = node.next
                    node.next.previous = node.previous
                return
            node = node.next

    def iter_forward(self):
        node = self.head
        while node:
            val = node.value
            node = node.next
            yield val

    def iter_backward(self):
        node = self.tail
        while node:
            val = node.value
            node = node.previous
            yield val

# Test Case
double_linked_list = DoubleLinkedList()
double_linked_list.append(5)
double_linked_list.append(7)
double_linked_list.append(-1)
double_linked_list.append(0.9)
double_linked_list.append(71)
iter_forward_test = []
for value in double_linked_list.iter_forward():
    iter_forward_test.append(value)
iter_backward_test = []
for value in double_linked_list.iter_backward():
    iter_backward_test.append(value)

print ("Pass" if (iter_forward_test == [5, 7, -1, 0.9, 71]) else "Fail")
print ("Pass" if (iter_backward_test == [71, 0.9, -1, 7, 5]) else "Fail")
double_linked_list.delete(-1)
iter_forward_test = []
for value in double_linked_list.iter_forward():
    iter_forward_test.append(value)
print ("Pass" if (iter_forward_test == [5, 7, 0.9, 71]) else "Fail")
