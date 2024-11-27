import time

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Measure Execution Times
def measure_time(arr):
    # Measure time for Merge Sort
    start_time = time.time()
    sorted_arr_merge = merge_sort(arr.copy())
    merge_time = time.time() - start_time
    
    # Measure time for Quick Sort
    start_time = time.time()
    sorted_arr_quick = quick_sort(arr.copy())
    quick_time = time.time() - start_time
    
    # Display results
    print(f"\nMerge Sort Result: {sorted_arr_merge}")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    
    print(f"\nQuick Sort Result: {sorted_arr_quick}")
    print(f"Quick Sort Time: {quick_time:.6f} seconds")

# Main Function with Simple User Input
def main():
    # Simple input: ask the user to enter a list of numbers separated by spaces
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    measure_time(arr)

if __name__ == "__main__":
    main()
