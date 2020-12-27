from collections import deque

class Node:

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"Node({self.value}, left:{self.left_child}, right:{self.right_child})"

    def __str__(self):
        return f"Node({self.value})"

class Queue():

    def __init__(self):
        self.q = deque()

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        s = "Queue:\n"
        if len(self.q) > 0:
            s += "  <enqueue here> "
            s += "..".join([f"<{str(item)}>" for item in self.q])
            s += " <dequeue here>"
        else:
            s += "<empty>"
        return s


class Stack():

    def __init__(self):
        self.list = list()

    def push(self,value):
        self.list.append(value)

    def peek(self):
        return self.list[-1]

    def pop(self):
        return self.list.pop()
    
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        s = "Stack:\n"
        if len(self.list) > 0:
            s += "  <top> "
            s += "..".join([f"<{str(item)}>" for item in self.list[::-1]])
            s += " <bottom>"
        else:
            s += "<empty>"
        return s

class Tree:

    def __init__(self,value=None):
        self.root = Node(value)
    
    def get_root(self):
        return self.root

    def __repr__(self):
        """
        Traverse the tree using BFS so we can print it's structure.
        """
        level = 0
        q = Queue()
        visit_order = list()
        node = self.root
        q.enq((node,level))
        while(len(q) > 0):
            node,level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level) )
                continue
            visit_order.append( (node, level) )
            if node.left_child is not None:
                q.enq( (node.left_child, level + 1 ))
            else:
                q.enq( (None, level + 1) )
            if node.right_child is not None:
                q.enq( (node.right_child, level + 1) )
            else:
                q.enq( (None, level + 1) )
                
        s = "\nTree:"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n  " + str(node)
                previous_level = level
        s += "\n"

        return s

def pre_order_iterative(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    
    if node == None:
        return []

    stack.push(node)

    while(not stack.is_empty()):

        node = stack.pop()
        visit_order.append(node.value)

        if node.right_child:
            stack.push(node.right_child)
        if node.left_child:
            stack.push(node.left_child)
        
    return visit_order

def in_order_iterative(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    
    if node == None:
        return []

    while(not stack.is_empty() or node):

        if node:
            stack.push(node)
            node = node.left_child
        else:
            node = stack.pop()
            visit_order.append(node.value)
            node = node.right_child
        
    return visit_order

def post_order_iterative(tree):
    visit_order = list()
    last_node_visited = None
    stack = Stack()
    node = tree.get_root()
    
    if node == None:
        return []

    while(not stack.is_empty() or node):

        if node:
            stack.push(node)
            node = node.left_child
        else:
            peek_node = stack.peek()
            if peek_node.right_child and last_node_visited != peek_node.right_child:
                node = peek_node.right_child
            else:
                visit_order.append(peek_node.value)
                last_node_visited = stack.pop()
        
    return visit_order

def pre_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            visit_order.append(node.value)
            traverse(node.left_child)
            traverse(node.right_child)

    traverse(tree.get_root())

    return visit_order

def in_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            traverse(node.left_child)
            visit_order.append(node.value)
            traverse(node.right_child)

    traverse(tree.get_root())

    return visit_order

def post_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            traverse(node.left_child)
            traverse(node.right_child)
            visit_order.append(node.value)
            
    traverse(tree.get_root())

    return visit_order

def bfs(tree):
    visit_order = list()
    q = Queue()
    # start at the root node and add it to the queue
    node = tree.get_root()
    q.enq(node)
    while len(q) > 0:
        node = q.deq()
        visit_order.append(node.value)
        if node.left_child:
            q.enq(node.left_child)
        if node.right_child:
            q.enq(node.right_child)
    return visit_order

# Test cases

# Nodes
node = Node("A")
node.left_child = Node("B")
node.right_child = Node("C")
print(f"Node: {node}")

# Trees
tree = Tree("D")
tree.get_root().left_child = Node("B")
tree.get_root().right_child = Node("E")
tree.get_root().left_child.left_child = Node("A")
tree.get_root().left_child.right_child = Node("C")
tree.get_root().right_child.right_child = Node("F")
print(tree)
print("DFS") 
print("  Iterative version") 
print("     pre-order: Pass" if (pre_order_iterative(tree) == ['D', 'B', 'A', 'C', 'E', 'F']) else "   pre-order: Fail")
print("      in-order: Pass" if (in_order_iterative(tree) == ['A', 'B', 'C', 'D', 'E', 'F']) else "    in-order: Fail")
print("    post-order: Pass" if (post_order_iterative(tree) == ['A', 'C', 'B', 'F', 'E', 'D']) else "  post-order: Fail")
print("  Recursive version")
print("     pre-order: Pass" if (pre_order(tree) == ['D', 'B', 'A', 'C', 'E', 'F']) else "   pre-order: Fail")
print("      in-order: Pass" if (in_order(tree) == ['A', 'B', 'C', 'D', 'E', 'F']) else "    in-order: Fail")
print("    post-order: Pass" if (post_order(tree) == ['A', 'C', 'B', 'F', 'E', 'D']) else "  post-order: Fail")
print("BFS") 
print("  Pass" if (bfs(tree) == ['D', 'B', 'E', 'A', 'C', 'F']) else "  Fail")
