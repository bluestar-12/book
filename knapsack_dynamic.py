def knapsack(Profits, Weights, W):
    # Number of items
    n = len(Profits)
    
    # Create a DP table with (n+1) rows and (W+1) columns. Initialize with 0s.
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):  # Iterate through items
        for w in range(1, W + 1):  # Iterate through all possible weights
            if Weights[i - 1] <= w:  # If the item can be included
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - Weights[i - 1]] + Profits[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]  # If the item can't be included, take previous value
    
    # The last cell contains the maximum profit
    return dp[n][W]

# Function to take user input for the knapsack problem
def get_user_input():
    # Input the number of items
    n = int(input("Enter the number of items: "))
    
    # Input the profits and weights
    Profits = []
    Weights = []
    
    for i in range(n):
        profit = int(input(f"Enter the profit for item {i + 1}: "))
        weight = int(input(f"Enter the weight for item {i + 1}: "))
        Profits.append(profit)
        Weights.append(weight)
    
    # Input the maximum weight of the knapsack
    W = int(input("Enter the capacity of the knapsack: "))
    
    # Call the knapsack function and print the maximum profit
    print("Maximum profit of the knapsack is:", knapsack(Profits, Weights, W))

# Call the function to get user input and compute the maximum profit
get_user_input()

# Enter the number of items: 4
# Enter the profit for item 1: 2
# Enter the weight for item 1: 3
# Enter the profit for item 2: 3
# Enter the weight for item 2: 4
# Enter the profit for item 3: 1
# Enter the weight for item 3: 6
# Enter the profit for item 4: 4
# Enter the weight for item 4: 5
# Enter the capacity of the knapsack: 8

# Time Complexity: O(n * W)
# Space Complexity: O(n * W)

