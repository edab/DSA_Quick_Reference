# Graphs

A **Graph** is an ordered pair of a set $V$ of vertices and a set $E$ of edges.

<img src='https://g.gravizo.com/svg?
  digraph G {
    rankdir=LR;
    A -> B -> E -> D -> C -> A;
    C -> B;
  }
'/>

Graphs can be **undirected**, when each edge can be traversed in both directions, or **directed**, where an edge can be traversed only in one direction and is represented with a arrow.

Graphs can be **weighted**, where a number is associated to each edge, that can be for example the cost of traversing that specific edge.

## Representation

Graphs can be represented in different ways, each one with its pros and cons.

- **Node object**: we can create an object that represent a node, with an edge list that contain all the other nodes connected.
- **Adjacency list**: at each index of the list, the adjacent nodes to that vertex are stored.
- **Adjacent matrix**: each row and column index represent a node, and a value of 1 is inserted into a cell when two vertices are connected. 

## Terminology

There is some specific terminology associated with the graph:

- **Node** or **Vertex**: the basic element of a graph containing data.
- **Edge**: a connection between two vertices.
- **Loop**: when an edge from a node is incident on itself.
- **Degree of a vertex**: number of vertices that are incident on a given vertex.
- **Adjacency**: connection of a node to its neighbor.
- **Path**: sequence of vertices connected by edges.
