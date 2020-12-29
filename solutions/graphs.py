class GraphNode(object):

    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self, new_node):
        self.children.append(new_node)
    
    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):

    def __init__(self, node_list):
        self.nodes = node_list

    def edge_list(self):

        edge_list = list()  # set give better result, but we use here 2D list
        visited = set()
        queue = [self.nodes[0]]
        
        # Visit graph using BFS
        while len(queue) > 0:

            current_node = queue.pop(0)
            visited.add(current_node)

            for child in current_node.children:
                # Since is an undirected graph, we check both ways
                source = current_node.value
                dest = child.value
                if [source, dest] not in edge_list and [dest, source] not in edge_list:
                    edge_list.append([source, dest])
                if child not in visited:
                    queue.append(child)

        return edge_list

    def adjacent_list(self):

        adjacent_list = list()
        visited = set()
        queue = [self.nodes[0]]
        
        # Visit graph using BFS
        while len(queue) > 0:

            current_node = queue.pop(0)
            visited.add(current_node)

            node_adjacent_list = list()

            for child in current_node.children:
                node_adjacent_list.append(child.value)
                if child not in visited:
                    queue.append(child)

            adjacent_list.append(node_adjacent_list)

        return adjacent_list

    def adjacent_matrix(self):

        node_list = [node.value for node in self.nodes]
        node_list.sort()
        matrix = list([[0 for x in range(len(node_list))] for x in range(len(node_list))])
        visited = set()
        queue = [self.nodes[0]]
        
        # Visit graph using BFS
        while len(queue) > 0:

            current_node = queue.pop(0)
            visited.add(current_node)

            for child in current_node.children:
                # Since is an undirected graph, we check both ways
                source_idx = node_list.index(current_node.value)
                dest_idx = node_list.index(child.value)
                matrix[source_idx][dest_idx] = 1
                matrix[dest_idx][source_idx] = 1
                if child not in visited:
                    queue.append(child)

        return node_list, matrix
        
    def add_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self, node1, node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


    def dfs_search(self, root_node, search_value):

        # Sets are faster for lookups
        visited = set()          

        # Start with a given root node
        stack = [root_node]                     
        
        # Repeat until the stack is empty
        while len(stack) > 0:                   
                
            # Pop out a node added recently
            current_node = stack.pop()     

            # Mark it as visited
            visited.add(current_node)

            if current_node.value == search_value:
                return current_node

            # Check all the neighbours
            for child in current_node.children:

                # If a node hasn't been visited and is not in the stack
                if (child not in visited) and (child not in stack):         
                    stack.append(child)

    def dfs_search_recursive(self, start_node, search_value):

        # Set to keep track of visited nodes
        visited = set()               
        return self.__dfs_recursion(start_node, visited, search_value)

    def __dfs_recursion(self, node, visited, search_value):
        
        if node.value == search_value:
            # Don't search in other branches, if found = True
            found = True
            return node
        
        visited.add(node)
        found = False
        result = None

        # Conditional recurse on each neighbour
        for child in node.children:
            if (child not in visited):
                result = self.__dfs_recursion(child, visited, search_value)
                    
                # Once the match is found, no more recurse 
                if found:
                    break

        return result

    def bfs_search(self, root_node, search_value):

        # Sets are faster for lookups
        visited = set()
        queue = [root_node]
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            visited.add(current_node)

            if current_node.value == search_value:
                return current_node

            for child in current_node.children:
                if child not in visited:
                    queue.append(child)

# Helper functions
def print_edge(edge_list):
    for edge in edge_list:
        print(f"  - {edge}")

def print_adjacent_list(adjacent_list):
    for neighbour in adjacent_list:
        print(f"  - {neighbour}")

def print_adjacent_matrix(nodes, matrix):
    # Print column headers
    print("    " + ' '.join(map(str, nodes)))
    index = 0
    for row in matrix:
        print(f"  {nodes[index]} " + ' '.join(map(str, row)))
        index += 1

# Test Cases
nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

# DFS Tests
print("DFS")
print("  Iterative version") 
print("     Search A from S: " + "Pass" if (graph1.dfs_search(nodeS, 'A') == nodeA) else "     Fail")
print("     Search S from S: " + "Pass" if (graph1.dfs_search(nodeS, 'S') == nodeS) else "     Fail")
print("     Search R from S: " + "Pass" if (graph1.dfs_search(nodeS, 'R') == nodeR) else "     Fail")
print("  Recoursive version") 
print("     Search A from G: " + "Pass" if (graph1.dfs_search_recursive(nodeG, 'A') == nodeA) else "     Fail")
print("     Search A from S: " + "Pass" if (graph1.dfs_search_recursive(nodeS, 'A') == nodeA) else "     Fail")
print("     Search S from P: " + "Pass" if (graph1.dfs_search_recursive(nodeP, 'S') == nodeS) else "     Fail")
print("     Search R from H: " + "Pass" if (graph1.dfs_search_recursive(nodeH, 'R') == nodeR) else "     Fail")

# BFS Tests
print("BFS")
print("     Search A from S: " + "Pass" if (graph1.bfs_search(nodeS, 'A') == nodeA) else "     Fail")
print("     Search S from P: " + "Pass" if (graph1.bfs_search(nodeP, 'S') == nodeS) else "     Fail")
print("     Search R from H: " + "Pass" if (graph1.bfs_search(nodeH, 'R') == nodeR) else "     Fail")

# Edge list tests
print("Edge list representation")
#print_edge(graph1.edge_list())
print("     Pass" if (graph1.edge_list() == [['S', 'R'], ['R', 'G'], ['R', 'A'], ['R', 'P'], ['G', 'A'], ['G', 'H'], ['P', 'H']]) else "     Fail")

# Adjacent list tests
print("Adjacent list representation")
#print_adjacent_list(graph1.adjacent_list())
print("     Pass" if (graph1.adjacent_list() == [['R'], ['G', 'A', 'P', 'S'], ['R', 'A', 'H'], ['R', 'G'], ['R', 'H'], ['R', 'G'], ['G', 'P'], ['G', 'P']]) else "     Fail")

# Adjacent matrix tests
print("Adjacent matrix representation")
nodes, matrix = graph1.adjacent_matrix()
#print_adjacent_matrix(nodes, matrix)
print("     Pass" if (matrix == [[0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0]]) else "     Fail")
