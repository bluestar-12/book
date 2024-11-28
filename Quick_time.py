import random
import time  # Importing the time module to measure execution time

# Function to swap two elements in an array
def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]

# Function to find the pivot index for QuickSort
def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr, swap_index, i)
    swap(arr, pivot_index, swap_index)
    return swap_index

# QuickSort function
def QuickSort(arr, l, r):
    if l < r:
        pivot_index = pivot(arr, l, r)
        QuickSort(arr, l, pivot_index - 1)
        QuickSort(arr, pivot_index + 1, r)
    return arr

# Generate 50 random integers
krr = [random.randint(1, 100) for _ in range(50)]

# Measure the execution time
start_time = time.time()  # Start time before the sorting operation
sorted_array = QuickSort(krr, 0, len(krr) - 1)  # Perform QuickSort
end_time = time.time()  # End time after sorting

# Calculate and print the execution time
execution_time = end_time - start_time
print("Sorted Array:", sorted_array)
print(f"Execution Time: {execution_time:.6f} seconds")

# Time Complexity: O(n log n) on average, O(n^2) in the worst case
# Space Complexity: O(log n) on average (due to recursion depth), O(n) in the worst case (due to recursion stack in worst case)
