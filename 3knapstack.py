def knapsack_greedy(weights, profits, capacity):
    ratios = [(profits[i] / weights[i], i) for i in range(len(weights))]
    
    # Sort based on the profit-to-weight ratio in descending order
    ratios.sort(reverse=True, key=lambda x: x[0])
    
    total_profit = 0
    total_weight = 0
    selected_items = []
    
    # Loop through the sorted items and select them based on capacity
    for ratio, i in ratios:
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            total_profit += profits[i]
            selected_items.append(f"Item {i + 1}")
    
    return total_profit, total_weight, selected_items


# Taking user input for weights, profits, and capacity
n = int(input("Enter the number of items: "))

weights = []
profits = []

print("Enter the weights of the items:")
for i in range(n):
    weight = int(input(f"Weight of item {i + 1}: "))
    weights.append(weight)

print("Enter the profits of the items:")
for i in range(n):
    profit = int(input(f"Profit of item {i + 1}: "))
    profits.append(profit)

capacity = int(input("Enter the capacity of the knapsack: "))

# Call the knapsack function with user inputs
profit, weight, items = knapsack_greedy(weights, profits, capacity)

# Display the result
print(f"\nTotal Profit: {profit}")
print(f"Total Weight: {weight}")
print(f"Selected Items: {', '.join(items)}")
