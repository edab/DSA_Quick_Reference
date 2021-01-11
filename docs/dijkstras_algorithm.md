# The Dijkstra's Algorithms

The **Dijkstra's Shortest Path First algorithm** is one solution to the problem of finding the shortest paths between nodes in a graph.

This algorithm implements a so called _Greedy solution_, since will follow the best possible choice at each step.

## Implementations

### Basic implementation

Python3 implementation: [dijkstra.py](../solutions/dijkstra.py)

**Note** - This implementation of the Dijkstra's algorithm is not very efficient. Currently it has a $O(|V|^2)$ time complexity.

## The Algorithm

- Declare and initialize result, unvisited, and path
    - Create a `result` dictionary, which is used to preserve the shortest distance for all nodes in the graph. The distance to all other nodes from the source is unknown, therefore is set to infinity.
    - Create a set `unvisited` containing nodes that have not been visited, initialized with all nodes of the graph. Start with the source node, where the distance from source to source itself is 0.
    - Create a `path` dictionary that keeps track of the previous node that can lead to the current node.

- As long as `unvisited` is non-empty, repeat the following:
    - Find the unvisited node having smallest known distance from the source node.
    - For the current node, find all the **unvisited neighbours**.
    - If the calculated distance is less than the already known distance saved in `result` dictionary, we update the distance as well as the path.
    - Remove the current node from the `unvisited` set.



## The code

First, we need a basic implementation of a _Undirected Acyclic Graph_ using an adjacency dictionary, that contain:
- _a set_ of nodes for efficient lookups
- _an Adjacency dictionary_ using a defaultdict(), so we can easly lookup at non existent keys.
- _a Distances dictionary_, that contain the solution.

```python
class Graph:
    def __init__(self):
        # A set cannot contain duplicate nodes
        self.nodes = set()                   
        # Defaultdict provides a default value for a key that does not exists
        self.neighbours = defaultdict(list)  
        # Dictionary where key are (source, dest) and value is the distance
        self.distances = {}                  

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        # Since the graph is undirected
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance    
```

### Optimized implementation

Python3 implementation: [dijkstra.py](../solutions/dijkstra_optimized.py)

**Note** - This implementation of the Dijkstra's algorithm is not very efficient. Currently it has a $O(|E| + |V| * log(|V|))$ time complexity.

## The Algorithm

- Declare `distances` and `shortest_distances` dictionaries:
    - Create a `distances` dictionary containing all the nodes of the graph that have not been visited, with a value of 0 if the source, Otherwise infinite.
    - Create an empty `shortest_distances` dictionary, which is used to preserve the shortest distance found so far.

- As long as `distances` is non-empty, repeat the following:
    - Sort the `distances` dictionary by ascending distance
    - Move the node with the smallest distance to the `shortest_distance` dictionary
    - For each `neighbour` of node:
      - If the distance is smaller than the already stored distance, update the distances dictionary.

## The code

We need some helper object, a `Graph`, a `GraphNode` and a `GraphEdge` to represent the graph:

```python
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
```

We can now implement the Dijkstra algorithm,

```python
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
```
