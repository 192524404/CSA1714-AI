def is_valid(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def color_map(graph, colors, assignment={}):
    if len(assignment) == len(graph):
        return assignment

    # Pick the next uncolored region
    uncolored = [node for node in graph if node not in assignment][0]

    for color in colors:
        if is_valid(uncolored, color, assignment, graph):
            assignment[uncolored] = color
            result = color_map(graph, colors, assignment)
            if result:
                return result
            del assignment[uncolored]  # Backtrack

    return None

# Graph representation (e.g., Map with 4 adjacent regions)
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q']
}
colors = ['Red', 'Green', 'Blue']

solution = color_map(graph, colors)
print("Map Coloring Solution:")
for region, color in solution.items():
    print(f"{region}: {color}")
