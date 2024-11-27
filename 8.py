import itertools
import sys


def tsp_brute_force(dist):
    n = len(dist)
    cities = list(range(n))
    min_cost = sys.maxsize

    
    for perm in itertools.permutations(cities[1:]):
        path = [0] + list(perm)  # Fix starting city as 0
        cost = calculate_cost(dist, path)
        min_cost = min(min_cost, cost)

    return min_cost


def calculate_cost(dist, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]]
    cost += dist[path[-1]][path[0]]  # Return to starting city
    return cost


def tsp_dynamic(dist):
    n = len(dist)
    dp = [[-1] * (1 << n) for _ in range(n)] 
    return tsp_dp_util(0, 1, dist, dp, n)


def tsp_dp_util(pos, visited, dist, dp, n):
    if visited == (1 << n) - 1: 
        return dist[pos][0]  

    if dp[pos][visited] != -1:
        return dp[pos][visited]

    min_cost = sys.maxsize
    for city in range(n):
        if not (visited & (1 << city)):  # If city is not visited
            new_cost = dist[pos][city] + tsp_dp_util(city, visited | (1 << city), dist, dp, n)
            min_cost = min(min_cost, new_cost)

    dp[pos][visited] = min_cost
    return min_cost


def tsp_nearest_neighbor(dist):
    n = len(dist)
    visited = [False] * n
    current_city = 0
    visited[current_city] = True
    total_cost = 0

    for _ in range(n - 1):
        next_city = -1
        min_cost = sys.maxsize

        
        for city in range(n):
            if not visited[city] and dist[current_city][city] < min_cost:
                min_cost = dist[current_city][city]
                next_city = city

        visited[next_city] = True
        total_cost += min_cost
        current_city = next_city

    total_cost += dist[current_city][0]  
    return total_cost


def main():
   
    n = int(input("Enter the number of cities: "))

   
    print("Enter the distance matrix:")
    dist = []
    for i in range(n):
        dist.append(list(map(int, input().split())))

    
    brute_force_result = tsp_brute_force(dist)
    dp_result = tsp_dynamic(dist)
    greedy_result = tsp_nearest_neighbor(dist)

    
    print("Brute-force result: ", brute_force_result)
    print("Dynamic Programming result: ", dp_result)
    print("Nearest Neighbor result: ", greedy_result)

if __name__ == "__main__":
    main()
