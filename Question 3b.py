'''
Question 3
b) Implement bellman ford algorithm and priority queue using maximum heap
'''

import heapq
from math import inf

def initialize_single_source(graph, source):
    """
    Initialize single-source distances for graph traversal.

    Args:
        graph (dict): Adjacency list representation of the graph.
        source: Starting vertex.

    Returns:
        dict: Dictionary with distances initialized from source vertex.
    """
    distance = {}
    for vertex in graph:
        distance[vertex] = inf  # Initialize all distances to infinity
    distance[source] = 0  # Set distance of source vertex to 0
    return distance

def relax(u, v, weight, distance, parent):
    """
    Relaxation step to update distances and parents.

    Args:
        u: Source vertex.
        v: Destination vertex.
        weight: Weight of the edge (u, v).
        distance (dict): Current distances.
        parent (dict): Current parent vertices.

    Returns:
        None
    """
    # Check if relaxing the edge (u, v) results in a shorter path to v
    if distance[v] > distance[u] + weight:
        distance[v] = distance[u] + weight
        parent[v] = u

def bellman_ford(graph, source):
    """
    Bellman-Ford algorithm for finding shortest paths.

    Args:
        graph (dict): Adjacency list representation of the graph.
        source: Starting vertex.

    Returns:
        tuple: (distance, parent) dictionaries.
    """
    distance = initialize_single_source(graph, source)
    parent = {vertex: None for vertex in graph}

    # Relax edges repeatedly (V-1 times)
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                relax(u, v, weight, distance, parent)

    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distance[v] > distance[u] + weight:
                raise ValueError("Graph contains a negative weight cycle")

    return distance, parent

def dijkstra(graph, source):
    """
    Dijkstra's algorithm with priority queue as maximum heap.

    Args:
        graph (dict): Adjacency list representation of the graph.
        source: Starting vertex.

    Returns:
        tuple: (distance, parent) dictionaries.
    """
    distance = initialize_single_source(graph, source)
    parent = {vertex: None for vertex in graph}
    visited = set()
    heap = []

    heapq.heappush(heap, (0, source))  # Push source vertex with distance 0 to the heap

    while heap:
        current_distance, u = heapq.heappop(heap)

        if u in visited:
            continue

        visited.add(u)

        for v, weight in graph[u].items():
            if distance[v] > current_distance + weight:
                distance[v] = current_distance + weight
                parent[v] = u
                heapq.heappush(heap, (-distance[v], v))  # Use negative distance for max heap

    return distance, parent

# Example usage of Bellman-Ford algorithm
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}
source = 'A'
distance, parent = bellman_ford(graph, source)
print("Bellman-Ford Algorithm:")
print("Source vertex:", source)
print("Vertex\tDistance\tParent")
for vertex in graph:
    print(vertex, "\t\t", distance[vertex], "\t\t", parent[vertex])
print()

# Example usage of Dijkstra's algorithm with priority queue
source = 'A'
distance, parent = dijkstra(graph, source)
print("Dijkstra's Algorithm:")
print("Source vertex:", source)
print("Vertex\tDistance\tParent")
for vertex in graph:
    print(vertex, "\t\t", distance[vertex], "\t\t", parent[vertex])
