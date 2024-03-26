def dfs(graph, start):
    visited = set()
    stack = [start]
    visited.add(start)

    while stack:
        node = stack.pop()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS traversal starting from node 'A':")
dfs(graph, 'A')