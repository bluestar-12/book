def floyd_warshall(graph):
    num_vertices = len(graph)

    dist = [[graph[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

num_vertices = int(input("Enter the number of vertices: "))

print("Enter the adjacency matrix (use a large number like 999 for infinity):")
graph = []

for i in range(num_vertices):
    row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
    graph.append(row)


shortest_paths = floyd_warshall(graph)


print("\nShortest path matrix:")
for row in shortest_paths:
    print(" ".join(map(str, row)))
