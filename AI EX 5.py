from collections import deque

def is_valid(m, c):
    # Valid if missionaries non-negative, <= 3, and not outnumbered on either bank
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if (m > 0 and m < c) or ((3 - m) > 0 and (3 - m) < (3 - c)):
        return False
    return True

def solve_missionaries_cannibals():
    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    
    queue = deque([(initial_state, [])])
    visited = {initial_state}
    
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    while queue:
        (m, c, boat), path = queue.popleft()
        
        if (m, c, boat) == goal_state:
            return path + [(m, c, boat)]
            
        for dm, dc in moves:
            if boat == 1:  # Left to Right
                new_state = (m - dm, c - dc, 0)
            else:          # Right to Left
                new_state = (m + dm, c + dc, 1)
                
            nm, nc, nb = new_state
            if is_valid(nm, nc) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [(m, c, boat)]))
                
    return None

solution = solve_missionaries_cannibals()
for state in solution:
    print(f"Left Bank -> Missionaries: {state[0]}, Cannibals: {state[1]},
            Boat: {'Left' if state[2] else 'Right'}")
