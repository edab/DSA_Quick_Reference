# Helper Code
from collections import defaultdict
import sys

class Graph:

    def __init__(self, adjacent_list = None):

        # A set cannot contain duplicate nodes
        self.nodes = set()                  

        # Defaultdict provides a default value for a key that does not exists
        self.neighbours = defaultdict(list)  

        # Dictionary where key are (source, dest) and value is the distance
        self.distances = {}

        if adjacent_list is not None:
            self._read_adjacent_list(adjacent_list)       

    def _read_adjacent_list(self, adjacent_list):
        for elem in adjacent_list:
            self.add_node(elem[0])
            self.add_node(elem[1])
            self.add_edge(elem[0], elem[1], elem[2])

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)
        
''' Find the shortest path from the source node to every other node in the given graph '''
def dijkstra(graph, source, is_debug = False):

    # Declare and initialize result, unvisited, and path
    result = {node:0 if node == source else sys.maxsize for node in graph.nodes}
    unvisited = set(graph.nodes)
    path = dict()

    # As long as unvisited is non-empty
    while unvisited:

        if (is_debug):
            print(f"Current unvisited list: {unvisited}")
            print(f"Current result dictionary: {result}")
            print(f"Current path dictionary: {path}")
            
        # Find the unvisited node having smallest known distance from the source node.
        min_node = None
        for node in unvisited:
            if node in result:                
                if min_node is None:       
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break

        if (is_debug):
            print(f"  Selected closer node {min_node}")
            
        current_distance = result[min_node]

        if (is_debug):
            print(f"    Distance: {current_distance}")
        
        # For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.
        for neighbour in graph.neighbours[min_node]:

            if(is_debug):
                print(f"    Search node neighbours (neighbour: {neighbour})")

            if neighbour in unvisited:

                distance = current_distance + graph.distances[(min_node, neighbour)]

                if (is_debug):
                    print(f"      Distance from {min_node} to {neighbour} is {distance}")
            
                # If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.        
                if ((neighbour not in result) or (distance < result[neighbour])):
                    
                    if (is_debug):
                        print(f"          The distance is less that the preceeding one, so we update the result and the path dictionaries")

                    result[neighbour] = distance

                    # We need to update also the path dictionary as well for the same key.
                    path[neighbour] = min_node

            else:

                if (is_debug):
                    print(f"        Node already visited")

        # Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result

# Tests cases

# Utility function
def Test_Dijkstra(test_name, adj_list, expected, is_debug = False):
    print(f"{test_name:>25s}: ", end = '')
    testGraph = Graph(adj_list)
    distances = dijkstra(testGraph, 'A')
    distances = dijkstra(testGraph, 'A')
    if distances == expected:
        print("Pass ", end = '')
    else:
        print(f"Fail: [distances: {distances}, result: {expected} ", end = '')

    if is_debug:
        print(dijkstra(testGraph, 'A'))
    else:
        print()

# Test 1
adj_list = [('A','B',3),('A','D',2),('B','D',4),('B','E',6),('B','C',1),('C','E',2),('E','D',1)]
expected = {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}
Test_Dijkstra("Test 1", adj_list, expected)

# Test 2
adj_list = [('A','B',5),('B','C',5),('A','C',10)]
expected = {'A': 0, 'C': 10, 'B': 5}
Test_Dijkstra("Test 2", adj_list, expected)

# Test 3
adj_list = [('A', 'B', 5), ('A', 'C', 4), ('D', 'C', 1), ('B', 'C', 2), ('A', 'D', 2), ('B', 'F', 2), ('C', 'F', 3), ('E', 'F', 2), ('C', 'E', 1)]
expected = {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}
Test_Dijkstra("Test 3", adj_list, expected)