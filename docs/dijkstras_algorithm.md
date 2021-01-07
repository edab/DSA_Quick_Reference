# The Dijkstra's Algorithms

The **Dijkstra's Shortest Path First algorithm** is one solution to the problem of finding the shortest paths between nodes in a graph.

Since the algorithm picks up the _best_ possible solution to a sub-problem available at the moment, it is defined as _Greedy_.

## The Algorithm

- Create a `result` dictionary, which is used to preserve the shortest distance for all nodes in the graph.

- Start with the source node, where the distance from source to source itself is 0.

- The distance to all other nodes from the source is unknown, therefore is set to infinity.

- Create a set `unvisited` containing nodes that have not been visited, initialized with all nodes of the graph.

- Create a `path` dictionary that keeps track of the previous node that can lead to the current node.

- As long as `unvisited` is non-empty, repeat the following:
  - Find the unvisited node having smallest known distance from the source node.
  - For the current node, find all the **unvisited neighbours**.
  - If the calculated distance of the **unvisited neighbour** is less than the already known distance in `result` dictionary, update the shortest distance in the `result` dictionary.
  - If there is an update in the `result` dictionary, update the `path` dictionary as well for the same key.
  - Remove the current node from the `unvisited` set.

**Note** - This implementation of the Dijkstra's algorithm is not very efficient. Currently it has a *O(n^2)* time complexity. 
