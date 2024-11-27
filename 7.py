def subset_sum(S, n, subset, target_sum, current_sum, index):
    # If current sum becomes equal to the target sum, print the subset
    if current_sum == target_sum:
        print("Subset found:", subset)
        return True
    
    # If current sum exceeds the target sum or no more elements left to process
    if current_sum > target_sum or index == n:
        return False

    # Initialize a flag to indicate if at least one subset was found
    found_any = False

    # Include the current element in the subset
    subset.append(S[index])

    # Recur for the next element by including it in the subset
    if subset_sum(S, n, subset, target_sum, current_sum + S[index], index + 1):
        found_any = True
    
    # Backtrack: remove the current element from the subset
    subset.pop()

    # Recur for the next element without including it in the subset
    if subset_sum(S, n, subset, target_sum, current_sum, index + 1):
        found_any = True
    
    return found_any

def find_all_subsets(S, d):
    subset = []
    found = subset_sum(S, len(S), subset, d, 0, 0)
    if not found:
        print(f"No subset found with sum {d}.")

# Input from the user
try:
    # Taking input as space-separated integers for the set
    S = list(map(int, input("Enter the set of positive integers (space-separated): ").split()))
    d = int(input("Enter the target sum (d): "))
    
    if d <= 0 or any(x <= 0 for x in S):
        print("Please enter positive integers only.")
    else:
        print(f"Set: {S}, Target sum: {d}")
        find_all_subsets(S, d)
except ValueError:
    print("Invalid input! Please enter integers only.")
