import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority Queue stores tuples of (f_score, current_node, path, g_score)
    open_list = [(heuristics[start], start, [start], 0)]
    visited = set()

    while open_list:
        f, current, path, g = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                g_new = g + weight
                f_new = g_new + heuristics[neighbor]
                heapq.heappush(open_list, (f_new, neighbor, path + [neighbor], g_new))

    return None, float('inf')

# Graph Representation
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'G': 1},
    'E': {'B': 5, 'G': 2},
    'F': {'C': 3, 'G': 6},
    'G': {}
}

# Heuristic values (estimated distance to Goal 'G')
heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 1,
    'E': 2,
    'F': 4,
    'G': 0
}

path, cost = a_star_search(graph, heuristics, 'A', 'G')
print(f"Shortest Path: {' -> '.join(path)}")
print(f"Total Path Cost: {cost}")
