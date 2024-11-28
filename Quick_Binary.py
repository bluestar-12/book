import random

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

# Perform QuickSort
sorted_array = QuickSort(krr, 0, len(krr) - 1)
print("Sorted Array:", sorted_array)

# Binary Search function
def Binary_search(arr, value):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == value:
            return "Element present"
        elif arr[m] < value:
            l = m + 1
        else:
            r = m - 1
    return "Element not present"

# Function to choose a number and perform binary search
def choose_num(sorted_array):
    print("Hey user, give a number to perform binary search:")
    try:
        n = int(input())
        print(Binary_search(sorted_array, n))
    except ValueError:
        print("Invalid input! Please enter an integer.")

choose_num(sorted_array)

# Time Complexity
# QuickSort - O(n log n) (best/average case)
# O(n²) (worst case)

# Binary Search - O(log n)

# Space Complexity
# QuickSort - O(log n) (best/average case)
# O(n) (worst case)

# Binary Search - O(1) (iterative) / O(log n) (recursive)
