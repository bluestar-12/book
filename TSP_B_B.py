import math

class TSPBranchAndBound:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.visited = [False] * self.n
        self.final_res = math.inf

    def bound(self, curr_path, curr_cost):
        # Estimate the lower bound for the current solution
        bound = curr_cost
        for i in range(self.n):
            if not self.visited[i]:
                bound += min(self.graph[i])  # Add the minimum edge for unvisited nodes
        return bound

    def tsp_branch_bound(self, curr_node, curr_cost, curr_path, count):
        if count == self.n:
            # Return to the start node and compute the cost
            curr_cost += self.graph[curr_node][0]
            self.final_res = min(self.final_res, curr_cost)
            return

        for next_node in range(self.n):
            if not self.visited[next_node]:
                self.visited[next_node] = True
                curr_path.append(next_node)
                bound = self.bound(curr_path, curr_cost + self.graph[curr_node][next_node])
                if bound < self.final_res:
                    self.tsp_branch_bound(next_node, curr_cost + self.graph[curr_node][next_node], curr_path, count + 1)
                curr_path.pop()
                self.visited[next_node] = False

    def solve(self):
        self.visited[0] = True
        curr_path = [0]
        self.tsp_branch_bound(0, 0, curr_path, 1)
        return self.final_res

# Function to get user input
def get_user_input():
    n = int(input("Enter the number of cities: "))
    
    # Initialize a graph with user inputs
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Enter distances from city {i+1} to all other cities (space-separated): ").split()))
        graph.append(row)
    
    tsp_solver = TSPBranchAndBound(graph)
    print(f"Optimal solution using Branch and Bound: {tsp_solver.solve()}")

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
