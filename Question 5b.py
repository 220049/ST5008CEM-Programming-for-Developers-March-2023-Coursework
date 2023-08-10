'''
Question 5b
A network consisting of n servers is connected in a tree structure, where the servers are numbered from 0 to n - 1 and there are n - 1 connections between them that only allow for one-way communication. A 2D array a is used to represent these connections, where a[i] = [ai, bi] represents a directed path from server ai to server bi. However, due to specific requirements, all traffic from each server must route to server 0. The task is to reorient some connections to ensure that each server has a path to server 0. The goal is to minimize the number of edges that need to be changed. It is guaranteed that every server must have a path to server 0 after the connections are reordered.
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0.'''





def minReorder(n, connections):
    """
    Calculate the minimum number of edge reversals required to ensure that each server has a path to server 0.

    Args:
        n (int): The number of servers.
        connections (List[List[int]]): A list of connections represented as pairs [ai, bi].

    Returns:
        int: The minimum number of edge reversals.
    """
    # Initialize a graph to represent the connections between servers.
    graph = [[] for _ in range(n)]
    for connection in connections:
        from_node, to_node = connection
        graph[from_node].append(to_node)               # Directional edge from from_node to to_node
        graph[to_node].append(-from_node)              # Negative value to indicate reversed edge

    # Initialize arrays to track visited nodes and the count of reversed edges.
    visited = [False] * n
    reverseCount = [0] * n

    def dfs(node):
        """
        Depth-first search to traverse the graph and count reversed edges.

        Args:
            node (int): The current node being visited.

        Returns:
            None
        """
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[abs(neighbor)]:
                if neighbor < 0:
                    reverseCount[node] += 1               # Increment reversed edge count for this node
                    neighbor = -neighbor
                dfs(neighbor)
                reverseCount[node] += reverseCount[neighbor]  # Update reversed edge count

    # Start DFS traversal from server 0.
    dfs(0)

    # Count the total number of servers that need edge reversals to reach server 0.
    totalReversals = sum(1 for count in reverseCount if count > 0)
    return totalReversals

# Example usage
n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
result = minReorder(n, connections)
print("Minimum number of reversals:", result)
