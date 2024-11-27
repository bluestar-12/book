
def floyd_warshall(graph):
   
    num_vertices = len(graph)

   
    dist = [[graph[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


graph = [
    [0, 3, 999, 7],
    [3, 0, 2, 1],
    [999, 2, 0, 4],
    [7, 1, 4, 0]
]


shortest_paths = floyd_warshall(graph)


print("Shortest path matrix:")
for row in shortest_paths:
    print(row)
