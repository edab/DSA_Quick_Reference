class Stack:

  def __init__(self, initial_size = 10):
    self.arr = [0 for _ in range(initial_size)]
    self.next_index = 0
    self.num_elements = 0

  def push(self, data):
    if self.next_index == len(self.arr):
      print("Out of space! Increasing array capacity ...")
      self._handle_stack_capacity_full()
    self.arr[self.next_index] = data
    self.next_index += 1
    self.num_elements += 1

  def peek(self):
    if self.is_empty():
      return None
    return self.arr[self.next_index - 1]

  def pop(self):
    if self.is_empty():
      self.next_index = 0
      return None
    self.next_index -= 1
    self.num_elements -= 1
    return self.arr[self.next_index]

  def size(self):
    return self.num_elements

  def is_empty(self):
    return self.num_elements == 0

  def _handle_stack_capacity_full(self):
    old_arr = self.arr
    self.arr = [0 for _ in range( 2* len(old_arr))]
    for index, element in enumerate(old_arr):
      self.arr[index] = element

# Test case
stack = Stack()
print ("Pass" if (stack.size() == 0) else "Fail")
print ("Pass" if (stack.is_empty() == True) else "Fail")
for i in range(11):
  stack.push(f"Elem{i}")
print ("Pass" if (stack.size() == 11) else "Fail")
print ("Pass" if (stack.is_empty() == False) else "Fail")
print ("Pass" if (stack.peek() == "Elem10") else "Fail")
print ("Pass" if (stack.pop() == "Elem10") else "Fail")
print ("Pass" if (stack.pop() == "Elem9") else "Fail")
