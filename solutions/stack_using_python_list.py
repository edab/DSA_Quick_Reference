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

# Test case
stack = Stack()
for i in range(10):
    stack.push(f"Elem{i}")

print ("Pass" if (stack.size() == 10) else "Fail")
stack.push("Elem60")
print ("Pass" if (stack.pop() == "Elem60") else "Fail")
print ("Pass" if (stack.pop() == "Elem9") else "Fail")
print ("Pass" if (stack.pop() == "Elem8") else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 9) else "Fail")

            