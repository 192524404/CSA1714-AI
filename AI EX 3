from collections import deque

def water_jug_problem(cap1, cap2, target):
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        j1, j2, path = queue.popleft()

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        current_path = path + [(j1, j2)]

        if j1 == target or j2 == target:
            return current_path

        # Next possible states
        next_states = [
            (cap1, j2),  # Fill Jug 1
            (j1, cap2),  # Fill Jug 2
            (0, j2),     # Empty Jug 1
            (j1, 0),     # Empty Jug 2
            # Pour Jug 1 into Jug 2
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),
            # Pour Jug 2 into Jug 1
            (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], current_path))

    return None

solution = water_jug_problem(4, 3, 2)
print("Steps to measure target volume:")
for state in solution:
    print(f"Jug 1: {state[0]}L, Jug 2: {state[1]}L")
