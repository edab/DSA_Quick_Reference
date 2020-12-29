# Graphs

A **Graph** is an ordered pair of a set $V$ of vertices and a set $E$ of edges and is a more generic data structure than a _tree_.

<img src='https://g.gravizo.com/svg?
  digraph G {
    rankdir=LR;
    A -> B -> E -> D -> C -> A;
    C -> B;
  }
'/>

Graphs can be **undirected**, when each edge can be traversed in both directions, or **directed**, where an edge can be traversed only in one direction and is represented with an arrow.

Graphs can be **weighted**, where a number is associated with each edge, that can be for example the cost of traversing that specific edge.

A **disconnected** graph will contain nodes that cannot be reached from some other nodes, and in a **fully connected** graph, there is at least one edge for each node present.

## Representation

Graphs can be represented in different ways, each one with its pros and cons.

- **Vertex object**: an object that represents a node, with an attribute like an edges list that contains all the other nodes connected.
- **Edge object**: an object that represents an edge, with an attribute like a node list that contains the two nodes connected by the edge.
- **Edge list**: a 2D list of edges represented by lists of two elements, the starting node and the ending node.
- **Adjacency list**: a 2D list of nodes, where at each index of the list there is a list of adjacent nodes.
- **Adjacent matrix**: each row and column index represent a source and a destination node, and a value of 1 in the matrix indicates that the nodes are connected.

## Terminology

There is some specific terminology associated with the graph:

- **Node** or **Vertex**: the basic elements of a graph containing data.
- **Edge**: a connection between two vertices.
- **Loop**: when an edge from a node is incident on itself.
- **Degree of a vertex**: number of vertices that are incident on a given vertex.
- **Adjacency**: connection of a node to its neighbour.
- **Path**: a sequence of vertices connected by edges.

## Operations

### Traversal

There are two fundamental techniques for graph traversal:

- **Depth First Search (DFC)**: where we follow one path as far as it will go.
- **Breadth First Search (BFS)**: where we look at all the node adjacent to one before moving on to the next level.

Both techniques are often used as a basis for developing more advanced algorithms on _Graphs_.

## Implementation

### Basic Graph Representations

### Traversing

_DFS_ and _BFS_ implementation are very similar to the one for _Trees_, but since there is no root node, there is no obvious place to start.

#### Depth First Search

The implementation of _DFS_ is based on a _stack_, and repeat the following operations:

1. Start from a node and sign as visited
2. Add the node to the stack
3. Peek an edge, follow it to a node, and mark it as seen and add it to the stack
4. as long as there are more edge and unseen nodes, we repeat that step
5. when we hit a node already seen, we go back and try another edge
6. if we finish the edge, we pop a node from the stack and continue from there

The runtime complexity is $O(|V| + |E|)$, where $V$ is the number of vertexes and $E$ is the number of edges.

Technically we visit each edge twice, one for explore and one for travelling back through it.

### Breadth First Search

The implementation of _BFS_ is based on a _queue_, and repeat the following operations:

1. Start from a node and sign as visited
2. Visit all adjacent nodes to it, and add it to the queue
3. We go back to the first node, visit all its adjacent nodes and add it to the queue

We can think on _BFS_ as we are constructing a tree, were the child of a node are all its adjacent nodes, and where we proceed to visit by levels.
