def dfs(graph, node, visited=None, traversal=None):
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []
        
    visited.add(node)
    traversal.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal)
            
    return traversal

# Graph Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal:", dfs(graph, 'A'))
