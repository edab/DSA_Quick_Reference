class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


    def dfs_search(self, root_node, search_value):

        visited = set()                         # Sets are faster for lookups
        
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

    # Solution
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

# To verify the graph, we print all the parent nodes and child nodes
for each in graph1.nodes:
    print('parent node = ',each.value,end='\nchildren\n')
    for each in each.children:
        print(each.value,end=' ')
    print('\n')

print("  Iterative version") 
print("     Pass" if (graph1.dfs_search(nodeS, 'A') == nodeA) else "     Fail")
print("     Pass" if (graph1.dfs_search(nodeS, 'S') == nodeS) else "     Fail")
print("     Pass" if (graph1.dfs_search(nodeS, 'R') == nodeR) else "     Fail")
print("  Recoursive version") 
print("     Pass" if (graph1.dfs_search_recursive(nodeG, 'A') == nodeA) else "     Fail")
print("     Pass" if (graph1.dfs_search_recursive(nodeS, 'A') == nodeA) else "     Fail")
print("     Pass" if (graph1.dfs_search_recursive(nodeP, 'S') == nodeS) else "     Fail")
print("     Pass" if (graph1.dfs_search_recursive(nodeH, 'R') == nodeR) else "     Fail")
