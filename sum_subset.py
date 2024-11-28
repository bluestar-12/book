def find_subset(arr, target):
    res = []

    # Backtracking function
    def backtrack(start, current_subset, current_sum):
        # If the current sum matches the target, add the current subset to the result
        if current_sum == target:
            res.append(list(current_subset))
            return
        
        # If the current sum exceeds the target, no need to proceed further
        if current_sum > target:
            return
        
        # Loop through the array starting from 'start' index
        for i in range(start, len(arr)):
            current_subset.append(arr[i])

            # Recursive call to continue with the next elements
            backtrack(i + 1, current_subset, current_sum + arr[i])

            # Backtrack by removing the last added element
            current_subset.pop()

    # Initial call to the backtracking function
    backtrack(0, [], 0)
    
    return res

# Function to take user input
def get_user_input():
    # Input the list of numbers
    nums = list(map(int, input("Enter the numbers separated by space: ").split()))
    
    # Input the target sum
    target = int(input("Enter the target sum: "))
    
    # Call the find_subset function and print the result
    subsets = find_subset(nums, target)
    if subsets:
        print("Here are all possible subsets that sum to", target, ":", subsets)
    else:
        print("No subsets found that sum to", target)

# Call the function to get user input and find subsets
get_user_input()

# Time Complexity:
# The time complexity for this backtracking approach is O(2^n), where n is the number of elements in the array.
# This is because we explore each possible subset of the input array, which has a total of 2^n subsets.
# The backtracking function explores all subsets by considering each element once.

# Space Complexity:
# The space complexity is O(n), where n is the number of elements in the array. This space is used by the
# recursive call stack and the current subset being built. The maximum depth of the recursion will be 'n',
# and each subset can take at most O(n) space in the worst case.
