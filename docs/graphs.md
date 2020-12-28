# Graphs

A **Graph** is an ordered pair of a set $V$ of vertices and a set $E$ of edges, and is a more generic data structure than a _tree_.

<img src='https://g.gravizo.com/svg?
  digraph G {
    rankdir=LR;
    A -> B -> E -> D -> C -> A;
    C -> B;
  }
'/>

Graphs can be **undirected**, when each edge can be traversed in both directions, or **directed**, where an edge can be traversed only in one direction and is represented with a arrow.

Graphs can be **weighted**, where a number is associated to each edge, that can be for example the cost of traversing that specific edge.

A **disconnected** graph will contain nodes that cannot be reached from some other nodes, and in a **fully connected** graph there is at least one edge for each node present.

## Representation

Graphs can be represented in different ways, each one with its pros and cons.

- **Vertex object**: an object that represent a node, with an attribute like an edges list that contain all the other nodes connected.
- **Edge object**: an object that represent an edge, with an attribute like a node list that contain the two nodes connected by the edge.
- **Edge list**: a 2D list of edges represented by lists of two elements, the starting node and the ending node.
- **Adjacency list**: a 2D list of nodes, where at each index of the list there is a list of adjacent nodes.
- **Adjacent matrix**: each row and column index represent a source and destination node, and a value of 1 in the matrix indicates that the node are connected.

## Terminology

There is some specific terminology associated with the graph:

- **Node** or **Vertex**: the basic element of a graph containing data.
- **Edge**: a connection between two vertices.
- **Loop**: when an edge from a node is incident on itself.
- **Degree of a vertex**: number of vertices that are incident on a given vertex.
- **Adjacency**: connection of a node to its neighbor.
- **Path**: sequence of vertices connected by edges.

## Operations

### Traversal

There are two fundamental technique for graph traversal:

- **Depth First Search (DFC)**: where we follow one path as far as it will go.
- **Breadth First Search (BFS)**: where we look at all the node adjacent to one before moving on to the next level.

Both techniques are often used as a basis for developing more advanced algorithms on _Graphs_.

## Implementation

### Basic Graph Representations

### Depth First Search

_DFS_ implementation is very similar to the one already seen on _Tree_, but since there is not root node, there is no obvious place to start.

Common implementation of _DFS_ uses stack, and repeat the following operations:

- we sign the node as visited
- we add the node to the stack
- we peek an edge, and follow it to a node, and mark it as seen and add it to the stack
- as long as there are more edge and unseen nodes, we repeat that step
- when we hit a node already seen, we go back and try another edge
- if we finish the edge, we pop a node from the stack and continue from there

The runtime complexity is $O(|V| + |E|)$, where $V$ is the number of vertex and $E$ is the number of edges.

Technically we visit each edge twice, one for explore and one for traveling back through it.
