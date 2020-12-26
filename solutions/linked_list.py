class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, values = []):
        
        self.head = None
        for value in values:
            self.append(value)

    def append(self, value):
        
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def search(self, value):
        
        if self.head is None:
            return False

        node = self.head
        while node:
            if node.value == value:
                return True 
            node = node.next
        
        return False

    def delete(self, value):
        
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

    def pop(self):

        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        return node.value

    def to_list(self):
        
        out = []
        node = self.head
        while node is not None:
            out.append(node.value)
            node = node.next
        return out

# Test Case
linked_list = LinkedList([5, 7, -1, 0.9, 71])
print("Linked List tests:")
print ("  Initialization: " + "Pass" if (linked_list.to_list() == [5, 7, -1, 0.9, 71]) else "Fail")
linked_list.delete(-1)
print ("          Delete: " + "Pass" if (linked_list.to_list() == [5, 7, 0.9, 71]) else "Fail")
print ("          Search: " + "Pass" if (linked_list.search(0.9)) else "Fail")
print ("          Search: " + "Pass" if (not linked_list.search(55)) else "Fail")
linked_list.append(91)
print ("          Append: " + "Pass" if (linked_list.to_list() == [5, 7, 0.9, 71, 91]) else "Fail")
print ("             Pop: " + "Pass" if (linked_list.pop() == 5) else "Fail")
