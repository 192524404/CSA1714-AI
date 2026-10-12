import math

def minimax(depth, node_index, is_maximizing, scores, height):
    # Terminal node reached
    if depth == height:
        return scores[node_index]

    if is_maximizing:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

# Leaf nodes (evaluations)
scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_height = math.floor(math.log2(len(scores)))

optimal_value = minimax(0, 0, True, scores, tree_height)
print(f"The optimal value found using Minimax is: {optimal_value}")
