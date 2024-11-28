def knapsack_backtracking(Profits, Weights, W):
    n = len(Profits)
    max_profit = 0

    # Function to explore all possibilities using backtracking
    def backtrack(i, current_weight, current_profit):
        nonlocal max_profit
        if current_weight <= W:
            max_profit = max(max_profit, current_profit)  # Update the maximum profit

        if i == n or current_weight >= W:  # If all items are considered or capacity is exceeded
            return

        # Case 1: Include the current item
        if current_weight + Weights[i] <= W:
            backtrack(i + 1, current_weight + Weights[i], current_profit + Profits[i])

        # Case 2: Exclude the current item
        backtrack(i + 1, current_weight, current_profit)

    # Start the backtracking process
    backtrack(0, 0, 0)

    return max_profit

# Function to take user input for the knapsack problem
def get_user_input_backtracking():
    n = int(input("Enter the number of items: "))
    Profits = []
    Weights = []
    for i in range(n):
        profit = int(input(f"Enter the profit for item {i + 1}: "))
        weight = int(input(f"Enter the weight for item {i + 1}: "))
        Profits.append(profit)
        Weights.append(weight)
    W = int(input("Enter the capacity of the knapsack: "))
    print("Maximum profit of the knapsack using Backtracking is:", knapsack_backtracking(Profits, Weights, W))

# Call the function to get user input and compute the maximum profit
get_user_input_backtracking()

# Time Complexity: O(2^n) because we explore all possible subsets of items
# Space Complexity: O(n) for storing the recursive call stack
