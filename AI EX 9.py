from itertools import permutations

def travelling_salesman_problem(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    
    min_path = float('inf')
    best_route = []
    
    for perm in permutations(vertices):
        current_weight = 0
        k = start
        route = [start]
        
        for next_node in perm:
            current_weight += graph[k][next_node]
            k = next_node
            route.append(k)
            
        current_weight += graph[k][start]  # Return to start city
        route.append(start)
        
        if current_weight < min_path:
            min_path = current_weight
            best_route = route
            
    return min_path, best_route

# Distance matrix graph
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

cost, path = travelling_salesman_problem(graph, 'A')
print(f"Minimum Distance: {cost}")
print(f"Optimal Path: {' -> '.join(path)}")
