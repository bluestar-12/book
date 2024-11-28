import random
import time  # Importing the time module to measure execution time

# Merge function to merge two halves of an array
def merge(arr, left, m, right):
    # Find the sizes of the two subarrays to be merged
    n1 = m - left + 1
    n2 = right - m
    
    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2
    
    # Copy data to temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]
    
    # Merge the temporary arrays back into arr[left..right]
    i = 0  # Initial index for left subarray
    j = 0  # Initial index for right subarray
    k = left  # Initial index for merged subarray
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# MergeSort function
def mergeSort(arr, left, right):
    if left < right:
        m = (left + right) // 2  # Using 'm' instead of 'middle'
        
        # Sort the first and second halves
        mergeSort(arr, left, m)
        mergeSort(arr, m + 1, right)
        
        # Merge the sorted halves
        merge(arr, left, m, right)
    
    return arr

# Generate 50 random integers
arr = [random.randint(1, 100) for _ in range(50)]

# Measure the execution time
start_time = time.time()  # Start time before the sorting operation
sorted_array = mergeSort(arr, 0, len(arr) - 1)  # Perform MergeSort
end_time = time.time()  # End time after sorting

# Calculate and print the execution time
execution_time = end_time - start_time
print("Sorted Array:", sorted_array)
print(f"Execution Time: {execution_time:.6f} seconds")

# Time Complexity: O(n log n) for both average and worst case
# Space Complexity: O(n) for the temporary arrays used during merging
