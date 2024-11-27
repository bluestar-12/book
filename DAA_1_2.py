import random

# Binary Search Function
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"Element found at index {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "Element not found"

# Main Function to Test Binary Search
def main():
    # Generate a sorted array of 500 random integers
    arr = random.sample(range(1, 1001), 500)
    arr.sort()  # Ensure the array is sorted for binary search

    print("Generated Sorted Array:")
    print(arr)
    
    # Take user input for the element to search
    target = int(input("\nEnter the element to search: "))
    
    # Perform binary search
    result = binary_search(arr, target)
    print(result)

if __name__ == "__main__":
    main()
