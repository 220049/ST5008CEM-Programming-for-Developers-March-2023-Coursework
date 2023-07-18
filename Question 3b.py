'''
Question 3
b) Implement bellman ford algorithm and priority queue using maximum heap
'''
import heapq
from math import inf


def initialize_single_source(graph, source):
    distance = {}
    for vertex in graph:
        distance[vertex] = inf
    distance[source] = 0
    return distance


def relax(u, v, weight, distance, parent):
    if distance[v] > distance[u] + weight:
        distance[v] = distance[u] + weight
        parent[v] = u


def bellman_ford(graph, source):
    distance = initialize_single_source(graph, source)
    parent = {vertex: None for vertex in graph}

    # Relax edges repeatedly
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
    distance = initialize_single_source(graph, source)
    parent = {vertex: None for vertex in graph}
    visited = set()
    heap = []

    heapq.heappush(heap, (0, source))

    while heap:
        current_distance, u = heapq.heappop(heap)

        if u in visited:
            continue

        visited.add(u)

        for v, weight in graph[u].items():
            if distance[v] > current_distance + weight:
                distance[v] = current_distance + weight
                parent[v] = u
                heapq.heappush(heap, (distance[v], v))

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

# Example usage of Dijkstra's algorithm with priority queue implemented as maximum heap
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}
source = 'A'
distance, parent = dijkstra(graph, source)
print("Dijkstra's Algorithm:")
print("Source vertex:", source)
print("Vertex\tDistance\tParent")
for vertex in graph:
    print(vertex, "\t\t", distance[vertex], "\t\t", parent[vertex])
