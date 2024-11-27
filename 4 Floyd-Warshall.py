# Floyd-Warshall Algorithm to find all pair shortest paths
def floyd_warshall(graph):
    # Get the number of vertices
    num_vertices = len(graph)

    # Initialize the distance matrix
    dist = [[graph[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    # Apply the Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Update the distance if a shorter path is found
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example graph represented as an adjacency matrix
# - A large value (e.g., 999) represents no direct path between nodes
graph = [
    [0, 3, 999, 7],
    [3, 0, 2, 1],
    [999, 2, 0, 4],
    [7, 1, 4, 0]
]

# Call the function
shortest_paths = floyd_warshall(graph)

# Display the result
print("Shortest path matrix:")
for row in shortest_paths:
    print(row)
