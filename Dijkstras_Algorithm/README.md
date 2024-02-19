## Dijkstra-s-Algorithm

Dijkstra's algorithm is a popular algorithm in graph theory used to find the shortest path between two nodes in a weighted graph.
It starts from a source node and explores the neighboring nodes, updating their costs and parents if a shorter path is found.

## Usage

Run 'dijkstras_algorithm.py'

The algorithm's main loop iterates through nodes, updating costs and parents as it explores the graph. The result is the shortest path from the start node to the destination.

start - > 'A' [ 6 ]

start - > 'B' [ 2 ]

'A' - > 'Fin' [ 1 ]

'B' - > 'A' [ 3 ]

'B' - > 'Fin' [ 5 ].

## Sample Output

Total shortest distance to reach final:  6

Parent of Destination:  a.

## Complexity Analysis

The time complexity of Dijkstra's algorithm is generally O((V + E) * log(V)), where V is the number of vertices and E is the number of edges.

The space complexity is O(V) for storing costs, parents, and the processed nodes list. In the case of a dense graph, where the number of edges approaches V^2, the space complexity may be O(V^2).
