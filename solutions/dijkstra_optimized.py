# Dijkstra's algorithm O(E + VlogV) implementation

# Helper Code
from collections import defaultdict
import math

class GraphEdge:
    
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance


class GraphNode:

    def __init__(self, val = None):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))


class Graph:

    def __init__(self, adjacent_list = None):

        self.nodes = defaultdict(GraphNode)                  

        if adjacent_list is not None:
            self._read_adjacent_list(adjacent_list)       

    def _read_adjacent_list(self, adjacent_list):
        for elem in adjacent_list:
            self.nodes[elem[0]].value = elem[0]
            self.nodes[elem[1]].value = elem[1]
            self.add_edge(self.nodes[elem[0]], self.nodes[elem[1]], elem[2])

    def add_edge(self, node1, node2, distance):
        if node1.value in self.nodes and node2.value in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)


def dijkstra(graph, start):
    
    # Dictionary with distances to all nodes, initially set all to infinity
    distances = {v:0 if k == start else math.inf for k, v in graph.nodes.items()}
    
    # Dictionary with the "shortest" distance to all nodes
    shortest_distance = {}
    
    while distances:
        
        # Sort the distances dictionary by ascending distance
        node, distance = sorted(distances.items(), key=lambda x: x[1])[0]
        
        # Move the node with the smallest distance to shortest_distance
        shortest_distance[node.value] = distances.pop(node)
        
        # For each neighbour of node, if the distance is smaller than the 
        # already stored distance, update the distances dictionary
        for edge in node.edges:
            if edge.node in distances:                
                distance_to_neighbour = distance + edge.distance
                if distances[edge.node] > distance_to_neighbour:
                    distances[edge.node] = distance_to_neighbour
                    
    return shortest_distance

# Tests cases

# Utility function
def Test_Dijkstra(test_name, adj_list, source, expected, is_debug = False):
    print(f"{test_name:>25s}: ", end = '')
    testGraph = Graph(adj_list)
    distances = dijkstra(testGraph, source)
    if distances == expected:
        print("Pass ", end = '')
    else:
        print(f"Fail: [distances: {distances}, expected: {expected} ", end = '')

    if is_debug:
        print(distances)
    else:
        print()

# Test 1
adj_list = [('A','C',4),('A','D',6),('A','B',3),('B','D',4),('C','E',7),('D','E',4),('D','F',5),('E','G',4),('F','G',5)]
expected = {'A': 0, 'B': 3, 'C': 4, 'D': 6, 'E': 10, 'F': 11, 'G': 14}
Test_Dijkstra("Test 1", adj_list, 'A', expected)

# Test 2
adj_list = [('A','B',5),('B','C',5),('A','C',10)]
expected = {'A': 0, 'C': 10, 'B': 5}
Test_Dijkstra("Test 2", adj_list, 'A', expected)

# Test 3
adj_list = [('A','B',3),('A','D',2),('B','D',4),('B','E',6),('B','C',1),('C','E',2),('E','D',1)]
expected = {'B': 0, 'C': 1, 'A': 3, 'E': 3, 'D': 4}
Test_Dijkstra("Test 3", adj_list, 'B', expected)
