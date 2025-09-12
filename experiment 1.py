from collections import deque

# Function to check if current state is goal
def is_goal(state, goal):
    return state == goal

# Function to get possible moves (up, down, left, right)
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)  # 0 represents the blank space
    row, col = divmod(idx, 3)

    # Possible moves: Up, Down, Left, Right
    moves = {
        'Up': (row - 1, col),
        'Down': (row + 1, col),
        'Left': (row, col - 1),
        'Right': (row, col + 1)
    }

    for move, (r, c) in moves.items():
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            new_state = list(state)
            # Swap blank with target
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append((tuple(new_state), move))

    return neighbors

# BFS Algorithm
def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()

        if is_goal(state, goal):
            return path

        for neighbor, move in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [move]))
    return None

# Main program
if __name__ == "__main__":
    # Start and Goal state
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)

    print("Start State:")
    for i in range(0, 9, 3):
        print(start[i:i+3])

    print("\nGoal State:")
    for i in range(0, 9, 3):
        print(goal[i:i+3])

    solution = bfs(start, goal)

    if solution:
        print("\nSolution found in", len(solution), "moves:")
        print(" -> ".join(solution))
    else:
        print("No solution exists.")
