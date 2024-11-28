class Item:
    def __init__(self, weight, profit):
        self.w = weight
        self.p = profit
        self.R = self.p / self.w  # profit-to-weight ratio

def knapSack(items, capacity):
    # Sort the items by their profit-to-weight ratio in descending order
    items.sort(key=lambda item: item.R, reverse=True)

    totalprofit = 0
    totalWeight = 0
    UnusedCapacity = 0

    # Iterate over the sorted items
    for item in items:
        if item.w + totalWeight <= capacity:
            totalWeight += item.w
            totalprofit += item.p
        else:
            UnusedCapacity = capacity - totalWeight
            totalprofit += (item.R) * UnusedCapacity
            break  # Once the capacity is filled, stop further processing

    return totalprofit

# Taking user input
def get_user_input():
    # Input the number of items
    n = int(input("Enter the number of items: "))
    
    items = []
    for i in range(n):
        # Taking weight and profit of each item from the user
        weight = int(input(f"Enter the weight of item {i+1}: "))
        profit = int(input(f"Enter the profit of item {i+1}: "))
        item = Item(weight, profit)
        items.append(item)
    
    # Input the capacity of the knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Calculate and print the maximum profit using knapSack
    max_profit = knapSack(items, capacity)
    print(f"The maximum profit is: {max_profit}")

# Calling the function to get input and calculate profit
get_user_input()

# Time Complexity:
# O(n log n)
# The dominant factor is the sorting of the items based on their profit-to-weight ratio, which takes O(n log n) time.
# Space Complexity:
# O(n)
# Space is required for storing the list of items, and the sorting algorithm uses O(n) space in the worst case 
