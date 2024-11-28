INF = 9999

def printSolution(nv, distance):
    # This function prints the shortest distance matrix
    for i in range(nv):
        for j in range(nv):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print("")

def floyd_warshall(nv, distance):
    # Floyd-Warshall algorithm to find the shortest paths
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                # Updating the distance matrix with minimum distance
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    # Printing the shortest path matrix
    printSolution(nv, distance)

# Function to take user input for the graph
def get_user_input():
    nv = int(input("Enter the number of vertices: "))  # Number of vertices
    distance = [[INF] * nv for _ in range(nv)]  # Initialize distance matrix with INF
    
    # Set diagonal to 0 as distance to itself is always 0
    for i in range(nv):
        distance[i][i] = 0
    
    # Input the edges
    num_edges = int(input(f"Enter the number of edges: "))
    
    print("Enter each edge with its weight in the format (u v w), where u and v are vertices and w is the weight:")
    for _ in range(num_edges):
        u, v, w = map(int, input().split())
        distance[u][v] = w
    
    # Call the Floyd-Warshall algorithm
    floyd_warshall(nv, distance)

# Call the function to get user input and calculate shortest paths
get_user_input()


# Enter the number of vertices: 4
# Enter the number of edges: 4
# Enter each edge with its weight in the format (u v w), where u and v are vertices and w is the weight:
# 0 1 8
# 0 3 1
# 1 2 1
# 2 0 4

# Time Complexity: O(n³)
# Space Complexity: O(n²)

