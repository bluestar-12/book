import math

def tsp_backtracking(graph, current_node, visited, count, cost, ans):
    if count == len(graph):
        # Return to the starting node to complete the tour
        cost += graph[current_node][0]
        ans[0] = min(ans[0], cost)
        return
    
    for next_node in range(len(graph)):
        if not visited[next_node]:
            visited[next_node] = True
            tsp_backtracking(graph, next_node, visited, count + 1, cost + graph[current_node][next_node], ans)
            visited[next_node] = False

def solve_tsp_backtracking(graph):
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    ans = [math.inf]  # To store the optimal solution
    tsp_backtracking(graph, 0, visited, 1, 0, ans)
    return ans[0]

# Function to get user input
def get_user_input():
    n = int(input("Enter the number of cities: "))
    
    # Initialize a graph with user inputs
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Enter distances from city {i+1} to all other cities (space-separated): ").split()))
        graph.append(row)
    
    print(f"Optimal solution using Backtracking: {solve_tsp_backtracking(graph)}")

# Get user input and solve the TSP
get_user_input()

# Example input:
# Number of cities: 4
# Enter distances from city 1 to all other cities (space-separated): 0 10 15 20
# Enter distances from city 2 to all other cities (space-separated): 10 0 35 25
# Enter distances from city 3 to all other cities (space-separated): 15 35 0 30
# Enter distances from city 4 to all other cities (space-separated): 20 25 30 0

# Time-O(n!)
# Space- O(n)
