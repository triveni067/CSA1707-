from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    q = deque()
    
    # Start from both jugs empty
    q.append((0, 0))  # (jug1, jug2)

    while q:
        jug1, jug2 = q.popleft()

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        print(f"Jug1: {jug1}  |  Jug2: {jug2}")

        # Goal check
        if jug1 == target:
            print("\n✅ Target achieved!")
            return

        # Generate next possible states
        next_states = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2

            # Pour jug1 → jug2
            (jug1 - min(jug1, jug2_capacity - jug2),
             jug2 + min(jug1, jug2_capacity - jug2)),

            # Pour jug2 → jug1
            (jug1 + min(jug2, jug1_capacity - jug1),
             jug2 - min(jug2, jug1_capacity - jug1))
        ]

        for state in next_states:
            if state not in visited:
                q.append(state)

# Example Run
water_jug_bfs(4, 3, 2)
