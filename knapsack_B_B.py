class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight  # profit-to-weight ratio for sorting

def knapsack_branch_bound(Items, W):
    # Sort the items by their profit-to-weight ratio in descending order
    Items.sort(key=lambda item: item.ratio, reverse=True)
    
    # Start with an empty knapsack and a max profit of 0
    n = len(Items)
    max_profit = 0
    current_weight = 0
    current_profit = 0

    # Bound the solution recursively
    def bound(i, current_weight, current_profit):
        if current_weight >= W:
            return 0  # No further benefit if we exceed the capacity
        total_profit = current_profit
        j = i
        while j < n and current_weight + Items[j].weight <= W:
            current_weight += Items[j].weight
            total_profit += Items[j].profit
            j += 1
        if j < n:
            total_profit += (W - current_weight) * Items[j].ratio
        return total_profit

    # Branching to explore each item
    def branch(i, current_weight, current_profit):
        nonlocal max_profit
        if i == n:
            max_profit = max(max_profit, current_profit)
            return

        # Case 1: Include the current item
        if current_weight + Items[i].weight <= W:
            branch(i + 1, current_weight + Items[i].weight, current_profit + Items[i].profit)

        # Case 2: Do not include the current item
        if bound(i + 1, current_weight, current_profit) > max_profit:
            branch(i + 1, current_weight, current_profit)

    # Start the branching process
    branch(0, current_weight, current_profit)

    return max_profit

# Function to take user input for the knapsack problem
def get_user_input_branch_bound():
    n = int(input("Enter the number of items: "))
    Items = []
    for i in range(n):
        profit = int(input(f"Enter the profit for item {i + 1}: "))
        weight = int(input(f"Enter the weight for item {i + 1}: "))
        Items.append(Item(weight, profit))
    W = int(input("Enter the capacity of the knapsack: "))
    print("Maximum profit of the knapsack using Branch and Bound is:", knapsack_branch_bound(Items, W))

# Call the function to get user input and compute the maximum profit
get_user_input_branch_bound()

# Time Complexity: O(n log n) for sorting + O(2^n) in the worst case for branching
# Space Complexity: O(n) for storing the items and the recursion call stack
