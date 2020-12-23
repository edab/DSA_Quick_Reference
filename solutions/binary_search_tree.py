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


class Tree():

    def __init__(self):
        self.root = None

    def find_min(self):
        node = self.root
        while node.left_child:
            node = node.left_child
        return node.value

    def insert(self, new_value):

        new_node = Node(new_value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            parent = None
    
            while True:
                parent = current
                if new_node.value < current.value:
                    current = current.left_child
                    if current is None:
                        parent.left_child = new_node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = new_node
                        return

    def delete(self, value):

        curr = self.root 
        prev = None
    
        # First check if the value is actually present in the BST. 
        while(curr != None and curr.value != value): 
            prev = curr 
            if curr.value < value: 
                curr = curr.right 
            else: 
                curr = curr.left_child
    
        # If the value is not found, there is nothing to delete
        if curr == None: 
            return 
    
        # Check if the node to be deleted has atmost one child 
        if curr.left_child == None or curr.right_child == None: 
                
            # newCurr will replace the node to be deleted 
            newCurr = None
    
            # if the left child does not exist. 
            if curr.left == None: 
                newCurr = curr.right 
            else: 
                newCurr = curr.left 
    
            # check if the node to be deleted is the root. 
            if prev == None: 
                return newCurr 
    
            # Check if the node to be deleted is prev's left or right child and 
            # then replace this with newCurr 
            if curr == prev.left: 
                prev.left = newCurr 
            else: 
                prev.right = newCurr 
    
            curr = None
    
        # node to be deleted has two children. 
        else: 

            p = None
            temp = None
    
            # Compute the inorder successor of curr. 
            temp = curr.right_child
            while(temp.left_child != None): 
                p = temp 
                temp = temp.left 
    
            # check if the parent of the inorder successor is the root or not. 
            # if it isn't, then make the left child of its parent equal to the 
            # inorder successor's right child. 
            if p != None: 
                p.left = temp.right 
    
            else: 
                
                # if the inorder successor was the root, then make the right 
                # child of the node to be deleted equal to the right child of 
                # the inorder successor. 
                curr.right_child = temp.right_child 
    
            curr.value = temp.value 
            temp = None

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
                
        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s

# Test cases
tree = Tree()
tree.insert(51)
tree.insert(23)
tree.insert(47)
tree.insert(2)
print(tree.find_min())

#print(f"""
#search for 8: {tree.search(8)}
#search for 2: {tree.search(2)}
#""")

print(tree)
print("  Pass" if (tree.find_min() == 2) else "  Fail")

tree.delete(23)
print(tree)
print(tree.find_min())