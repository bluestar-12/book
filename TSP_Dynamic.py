import math

def tsp_dp(graph):
    n = len(graph)
    dp = [[math.inf] * (1 << n) for _ in range(n)]  # DP table
    dp[0][1] = 0  # Starting point, only visited node 0

    # Iterate through all subsets and all ending nodes
    for mask in range(1, 1 << n):
        for u in range(n):
            if mask & (1 << u):  # If the node u is in the current subset
                prev_mask = mask ^ (1 << u)
                for v in range(n):
                    if prev_mask & (1 << v):
                        dp[u][mask] = min(dp[u][mask], dp[v][prev_mask] + graph[v][u])

    # Find the optimal tour by returning to the starting point (node 0)
    min_tour_cost = min(dp[i][(1 << n) - 1] + graph[i][0] for i in range(1, n))
    
    return min_tour_cost

# Function to get user input
def get_user_input():
    n = int(input("Enter the number of cities: "))
    
    # Initialize a graph with user inputs
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Enter distances from city {i+1} to all other cities (space-separated): ").split()))
        graph.append(row)
    
    print(f"Optimal solution using Dynamic Programming: {tsp_dp(graph)}")

# Get user input and solve the TSP
get_user_input()

# Example input:
# Number of cities: 4
# Enter distances from city 1 to all other cities (space-separated): 0 10 15 20
# Enter distances from city 2 to all other cities (space-separated): 10 0 35 25
# Enter distances from city 3 to all other cities (space-separated): 15 35 0 30
# Enter distances from city 4 to all other cities (space-separated): 20 25 30 0

# Time Complexity-  O(n^2⋅2^n)
# Space complexity-  O(n⋅2^n)
