# Least Recently Used Cache
#
# The LRU caching scheme remove the least recently used data when the cache is full and a new page is referenced which is not there in cache.
#
# We use two data structures to implement an LRU Cache:
# - Double Linked List: The maximum size of the queue will be equal to the total number of frames available (cache size). The most recently used pages will be near front end and least recently pages will be near the rear end.
# - HashMap: a Hash with page number as key and address of the corresponding queue node as value.
#
# When a page is referenced, the required page may be in the memory:
# - If it is in the memory, we need to detach the node of the list and bring it to the front of the queue.
# - If the required page is not in memory, we add a new node to the front of the queue and update the corresponding node address in the hash.
# - If the queue is full, we remove a node from the rear of the queue, and add the new node to the front of the queue.

class Node:
    '''Double Linked List node implemetation for handling LRU Cache data'''
    
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"Node({self.key}, {self.value})"
    
    def __str__(self):
        return f"Node({self.key}, {self.value})"


class Deque:
    '''Deque implementation using Double Linked List, with a method to keep track of nodes access.'''

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, new_node):
        '''Nodes are enqueued on tail (newtest pointer)'''
        if self.tail is None:
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node

        self.num_elements += 1
            
    def dequeue(self):
        '''Nodes are dequeued on head (oldest poitner)'''
        if self.head is None:
            return None
        else:
            key = self.head.key
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.num_elements -= 1
            return key

    def access(self, node):
        '''An access should deque a random node and enqueue again'''
        
        if node is None or self.tail == node:
            # Base cases
            return
        
        if self.head == node:
            # If is the oldest, move the Head
            self.head = node.next
            self.head.prev = None
        else:
            # Otherwise, detach the node
            node.prev.next = node.next
            node.next.prev = node.prev

        # Link the node to the Tail
        self.tail.next = node
        node.prev = self.tail
        node.next = None

        # Move the Tail
        self.tail = node
        
    def size(self):
        return self.num_elements

    def to_list(self):
        output = list()
        node = self.head
        while node:
            node_tuple = tuple([node.key, node.value])
            output.append(node_tuple)
            node = node.next
        return output

    def __repr__(self):
        if self.num_elements > 0:
            s = "(Oldest) : "
            node = self.head
            while node:
                s += str(node)
                if node.next is not None:
                    s += ", "
                node = node.next
            s += " (Newest)"
            return s
        else:
            return "Deque: empty!"


class LRU_Cache(object):
    '''LRU Cache data object implementation with O(1) time complexity'''

    def __init__(self, capacity: int):
        # Initialize class variables
        self.lru_dict = dict()
        self.lru_deque = Deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # Retrieve item from provided key, using the hash map. Return -1 if nonexistent.
        if key in self.lru_dict:
            node = self.lru_dict[key]
            self.lru_deque.access(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
     
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.lru_dict:

            if self.capacity < 1:
                return -1

            if self.lru_deque.size() >= self.capacity:
                # Quick access the oldest element by using the deque
                old_node = self.lru_deque.dequeue()
                del self.lru_dict[old_node]

            new_node = Node(key, value)
            self.lru_deque.enqueue(new_node)
            self.lru_dict[key] = new_node
        else:
            node = self.lru_dict[key]
            node.value = value
            self.lru_deque.access(node)
            
    def to_list(self):
        return self.lru_deque.to_list()

    def __repr__(self):
        if self.lru_deque.num_elements > 0:
            s = "LRU_Cache: (Oldest) : "
            node = self.lru_deque.head
            while node:
                s += str(node)
                if node.next is not None:
                    s += ", "
                node = node.next
            s += " (Newest)"
            return s
        else:
            return "LRU_Cache: empty!"

# Tests cases

# Utility function
def Test_LRU_Cache(test_name, op_list, val_list, result_list, debug=False):

    lru_cache = None
    out_list = []

    print(f"{test_name:>25s}: ", end = '')

    # Use the operations
    for op, val, res in zip(op_list, val_list, result_list):
        out = None
        if op == "LRUCache":
            lru_cache = LRU_Cache(val[0])
        elif op == "put":
            lru_cache.put(val[0], val[1])
        elif op == "get":
            out = lru_cache.get(val[0])
        out_list.append(out)
        if out != res:
            print(f"Fail: [LRU Cache content: {lru_cache.to_list()}, op: {op}, val: {val}, res: {res}")
            return
        if debug and op != "LRUCache":
            print(f"  {op}({val}), dict: {len(lru_cache.lru_dict)}, deque: {lru_cache.lru_deque.size()}")
            print(f"    dict: {lru_cache.lru_dict}")
            print(f"   deque: {lru_cache.lru_deque}")
    
    print("Pass")


# Check LRU_Cache
print("\nTesting LRU Cache with access control\n")

# Test Miss LRU access
op_list = ["LRUCache","get"]
val_list = [[5],[1]]
result_list = [None,-1,]
Test_LRU_Cache("Miss LRU access", op_list, val_list, result_list)

# Test Exceed LRU capacity
op_list = ["LRUCache","put","put","put","put","put","get","get"]
val_list = [[3],[1,11],[2,22],[3,33],[4,44],[5,55],[2],[3]]
result_list = [None,None,None,None,None,None,-1,33]
Test_LRU_Cache("Exceed LRU capacity", op_list, val_list, result_list)

# Test Access central element
op_list = ["LRUCache","put","put","put","put","put","get"]
val_list = [[5],[1,11],[2,22],[3,33],[4,44],[5,55],[3]]
result_list = [None,None,None,None,None,None,33]
Test_LRU_Cache("Access central element", op_list, val_list, result_list)

# Test Access last element
op_list = ["LRUCache","put","put","put","put","put","get"]
val_list = [[5],[1,11],[2,22],[3,33],[4,44],[5,55],[5]]
result_list = [None,None,None,None,None,None,55]
Test_LRU_Cache("Access last element", op_list, val_list, result_list)

# Test Access first element
op_list = ["LRUCache","put","put","put","put","put","get"]
val_list = [[5],[1,11],[2,22],[3,33],[4,44],[5,55],[1]]
result_list = [None,None,None,None,None,None,11]
Test_LRU_Cache("Access first element", op_list, val_list, result_list)

# Test for updating value
op_list = ["LRUCache","put","get","put","get"]
val_list = [[5],[1,1],[2],[1,11111],[1]]
result_list = [None,None,-1,None,11111]
Test_LRU_Cache("Updating value", op_list, val_list, result_list)

# Test for zero capacity
op_list = ["LRUCache","put","get"]
val_list = [[0],[1,1],[1]]
result_list = [None,None,-1]
Test_LRU_Cache("Zero capacity", op_list, val_list, result_list)

# Test Update 2
op_list = ["LRUCache","put","put","put","get","put","get","put","get","get","get","get"]
val_list = [[2],[1,1],[2,2],[2,3],[2],[3,3],[2],[4,4],[1],[2],[3],[4]]
result_list = [None,None,None,None,3,None,3,None,-1,3,-1,4]
Test_LRU_Cache("Update 2", op_list, val_list, result_list)

# Test One element Deque add
op_list = ["LRUCache","put","get","put","get","get"]
val_list = [[1],[2,1],[2],[3,2],[2],[3]]
result_list = [None,None,1,None,-1,2]
Test_LRU_Cache("One element Deque add", op_list, val_list, result_list)

# Test Update and get
op_list = ["LRUCache","put","put","put","put","get","get"]
val_list = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
result_list = [None, None, None, None, None, -1, 3]
Test_LRU_Cache("Update and get", op_list, val_list, result_list)

# Test Long list
op_list = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
val_list = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
result_list = [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None, -1, 5, -1, 12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, -1, None, -1, 24, None, None, 18, None, None, None, None, -1, None, None, 18, None, None, -1, None, None, None, None, None, 18, None, None, -1, None, 4, 29, 30, None, 12, -1, None, None, None, None, 29, None, None, None, None, 17, 22, 18, None, None, None, -1, None, None, None, 20, None, None, None, -1, 18, 18, None, None, None, None, 20, None, None, None, None, None, None, None]
Test_LRU_Cache("Long list", op_list, val_list, result_list)

