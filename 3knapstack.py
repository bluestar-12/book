
def knapsack_greedy(weights, profits, capacity):
   
    ratios = [(profits[i] / weights[i], i) for i in range(len(weights))]
    
    
    ratios.sort(reverse=True, key=lambda x: x[0])
    
    total_profit = 0
    total_weight = 0
    selected_items = []
    
   
    for ratio, i in ratios:
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            total_profit += profits[i]
            selected_items.append(f"Item {i + 1}")
    
    return total_profit, total_weight, selected_items


weights = [3, 5, 5, 8, 4]
profits = [10, 20, 21, 30, 16]
capacity = 20


profit, weight, items = knapsack_greedy(weights, profits, capacity)


print(f"Total Profit: {profit}")
print(f"Total Weight: {weight}")
print(f"Selected Items: {', '.join(items)}")
