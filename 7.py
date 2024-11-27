def subset_sum(S, n, subset, target_sum, current_sum, index):
    
    if current_sum == target_sum:
        print("Subset found:", subset)
        return True
    
    
    if current_sum > target_sum or index == n:
        return False

   
    found_any = False

   
    subset.append(S[index])

   
    if subset_sum(S, n, subset, target_sum, current_sum + S[index], index + 1):
        found_any = True
    
   
    subset.pop()

    
    if subset_sum(S, n, subset, target_sum, current_sum, index + 1):
        found_any = True
    
    return found_any

def find_all_subsets(S, d):
    subset = []
    found = subset_sum(S, len(S), subset, d, 0, 0)
    if not found:
        print(f"No subset found with sum {d}.")


try:
    
    S = list(map(int, input("Enter the set of positive integers (space-separated): ").split()))
    d = int(input("Enter the target sum (d): "))
    
    if d <= 0 or any(x <= 0 for x in S):
        print("Please enter positive integers only.")
    else:
        print(f"Set: {S}, Target sum: {d}")
        find_all_subsets(S, d)
except ValueError:
    print("Invalid input! Please enter integers only.")
