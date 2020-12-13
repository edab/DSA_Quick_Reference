

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def to_list(self):
        out_list = []
        node = self.head

        while node:
            out_list.append(node.value)
            node = node.next

        return out_list

    def size(self):
        count = 1
        node = self.head

        if node == None:
            return 0

        while node.next:
            count += 1
            node = node.next

        return count

    def iter(self):
        node = self.head

        while node:
            val = node.value
            node = node.next
            yield val

    def delete(self, value):
        node = self.head
        prev = self.head

        while node:
            if node.value == value:
                if node == self.head:
                    self.head == node.next
                else:
                    prev.next = node.next
                return
            prev = node
            node = node.next

    def search(self, value):
        node = self.head

        while node:
            if node.value == value:
                return True
            node = node.next

        return False

# Test Case
linked_list = LinkedList()
linked_list.append(5)
linked_list.append(7)
linked_list.append(-1)
linked_list.append(0.9)
linked_list.append(71)
iter_test = []
for value in linked_list.iter():
    iter_test.append(value)

print ("Pass" if (linked_list.to_list() == [5, 7, -1, 0.9, 71]) else "Fail")
print ("Pass" if (linked_list.size() == 5) else "Fail")
print ("Pass" if (iter_test == [5, 7, -1, 0.9, 71]) else "Fail")
linked_list.delete(-1)
print ("Pass" if (linked_list.to_list() == [5, 7, 0.9, 71]) else "Fail")
print ("Pass" if (linked_list.search(99) == False) else "Fail")
print ("Pass" if (linked_list.search(7) == True) else "Fail")
