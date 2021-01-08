# The Dijkstra's Algorithms

The **Dijkstra's Shortest Path First algorithm** is one solution to the problem of finding the shortest paths between nodes in a graph.

Since the algorithm picks up the _best_ possible solution to a sub-problem available at the moment, it is defined as _Greedy_.

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

**Note** - This implementation of the Dijkstra's algorithm is not very efficient. Currently it has a *O(n^2)* time complexity.

## Implementations

Python3 implementation: [dijkstra.py](../solutions/dijkstra.py)

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
