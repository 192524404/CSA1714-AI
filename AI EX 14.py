def alphabeta(depth, node_index, is_maximizing, values, alpha, beta, height):
    if depth == height:
        return values[node_index]

    if is_maximizing:
        best = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, values, alpha, beta, height)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Beta Pruning
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, values, alpha, beta, height)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha Pruning
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
height = 3
result = alphabeta(0, 0, True, values, float('-inf'), float('inf'), height)
print(f"Optimal value with Alpha-Beta Pruning: {result}")
