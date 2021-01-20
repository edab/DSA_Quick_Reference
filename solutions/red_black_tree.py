class Node:

    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)

class RedBlackTree:

    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def _grandparent(self, node):
        """
        Helper method for finding the node's grand parent
        """
        if node.parent == None:
            return None
        return node.parent.parent

    
    def _pibling(self, node):
        """
        Helper method for finding the node's parent's sibling
        """
        p = node.parent
        gp = self._grandparent(node)
        if gp == None:
            return None
        if p == gp.left:
            return gp.right
        if p == gp.right:
            return gp.left

    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):
        
        # Case 1: Insert the Root Node
        if node.parent == None:
            return
        
        # Case 2: Insert the node at a Black Parent
        if node.parent.color == 'black':
            return

        # Case 3: Parent and Sibling are both Red
        if self._pibling(node) and self._pibling(node).color == 'red':
            self._pibling(node).color = 'black'
            node.parent.color = 'black'
            self._grandparent(node).color = 'red'
            return self.rebalance(self._grandparent(node))

        # If there is no gp, we have done
        gp = self._grandparent(node)
        if gp == None:
            return

        # Case 4: Parent is Red and Sibling is NULL Black
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right

        # Case 5: Parent and Child are both Red and on the same side of 
        #         their parent
        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'

    def rotate_left(self, node):

        # Save parent and sub-tree references
        p = node.parent
        node_moving_up = node.right

        # After 'node' moves up, swap right and left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # We connect to the sub-tree's parent
        # Maybe 'node' have been the root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):

        # Save parent and sub-tree references
        p = node.parent
        node_moving_up = node.left

        # After 'node' moves up, swap right and left child
        node.left = node_moving_up.right
        
        # 'node' moves down, to being a right child
        node_moving_up.right = node
        node.parent = node_moving_up
        
        # We connect to the sub-tree's parent
        # Maybe 'node' have been the root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def search(self, find_val):
        return False

    def __repr__(self):
        return 'RedBlackTree:\n\n' + self._repr_helper(self.root)

    def _repr_helper(self, node, level=0):
        s = '   ' + '   ' * (level - 1) + '+--' * (level > 0) + f'{node}\n'
        if node.left:
            s += self._repr_helper(node.left, level + 1)
        if node.right:
            s += self._repr_helper(node.right, level + 1)
        return s

# Test cases
tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)
print(tree)
tree.insert(13)
print(tree)
tree.insert(16)
print(tree)