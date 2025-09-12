import itertools

# Example: Distance matrix for 4 cities (A, B, C, D)
# Matrix[i][j] = distance from city i to city j
distance_matrix = [
    [0, 10, 15, 20],  # Distances from A
    [10, 0, 35, 25],  # Distances from B
    [15, 35, 0, 30],  # Distances from C
    [20, 25, 30, 0]   # Distances from D
]

cities = [0, 1, 2, 3]  # 0=A, 1=B, 2=C, 3=D

min_path = None
min_cost = float('inf')

# Generate all possible routes (permutations)
for perm in itertools.permutations(cities):
    cost = 0
    # Calculate total cost of visiting cities in this order
    for i in range(len(perm)-1):
        cost += distance_matrix[perm[i]][perm[i+1]]
    cost += distance_matrix[perm[-1]][perm[0]]  # return to start

    if cost < min_cost:
        min_cost = cost
        min_path = perm

# Print result
city_names = ['A', 'B', 'C', 'D']
path_str = " -> ".join(city_names[i] for i in min_path)
print(f"Shortest Path: {path_str} -> {city_names[min_path[0]]}")
print(f"Minimum Cost: {min_cost}")
