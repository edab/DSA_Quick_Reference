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

# Test case
stack = Stack()
for i in range(10):
    stack.push(f"Elem{i}")

print ("Pass" if (stack.size() == 10) else "Fail")
print ("Pass" if (stack.peek() == "Elem9") else "Fail")
stack.push("Elem60")
print ("Pass" if (stack.pop() == "Elem60") else "Fail")
print ("Pass" if (stack.pop() == "Elem9") else "Fail")
print ("Pass" if (stack.pop() == "Elem8") else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 12) else "Fail")
