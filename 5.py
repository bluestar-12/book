from queue import PriorityQueue


def knapsack_dp(weights, values, capacity):
    n = len(values)
   
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    
   
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

   
    return dp[n][capacity]



def knapsack_backtrack(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    
    if weights[n - 1] > capacity:
        return knapsack_backtrack(weights, values, capacity, n - 1)
    
    else:
        include = values[n - 1] + knapsack_backtrack(weights, values, capacity - weights[n - 1], n - 1)
        exclude = knapsack_backtrack(weights, values, capacity, n - 1)
        return max(include, exclude)



class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound
    
    
    def __lt__(self, other):
        return self.bound > other.bound

def bound(u, n, capacity, items):
    if u.weight >= capacity:
        return 0
    profit_bound = u.profit
    j = u.level + 1
    totweight = u.weight

    while j < n and totweight + items[j].weight <= capacity:
        totweight += items[j].weight
        profit_bound += items[j].value
        j += 1

    if j < n:
        profit_bound += (capacity - totweight) * items[j].ratio

    return profit_bound

def knapsack_branch_bound(weights, values, capacity):
    n = len(values)
    items = [Item(values[i], weights[i]) for i in range(n)]
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    pq = PriorityQueue()
    u = Node(-1, 0, 0, 0)
    v = Node(-1, 0, 0, 0)
    pq.put(u)
    
    maxProfit = 0

    while not pq.empty():
        u = pq.get()
        
        if u.level == -1:
            v.level = 0
        if u.level == n - 1:
            continue

        v.level = u.level + 1
        v.weight = u.weight + items[v.level].weight
        v.profit = u.profit + items[v.level].value

        if v.weight <= capacity and v.profit > maxProfit:
            maxProfit = v.profit
        
        v.bound = bound(v, n, capacity, items)

        if v.bound > maxProfit:
            pq.put(v)

        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v, n, capacity, items)

        if v.bound > maxProfit:
            pq.put(v)

    return maxProfit



values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("Dynamic Programming Result: ", knapsack_dp(weights, values, capacity))
n = len(values)
print("Backtracking Result: ", knapsack_backtrack(weights, values, capacity, n))
print("Branch and Bound Result: ", knapsack_branch_bound(weights, values, capacity))
