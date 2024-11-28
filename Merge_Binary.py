import random

# Merge function for MergeSort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    # Fill the left and right subarrays
    for i in range(n1):
        L[i] = arr[l + i]
    
    for j in range(n2):
        R[j] = arr[m + 1 + j]
    
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy remaining elements of L if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    # Copy remaining elements of R if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# MergeSort function
def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr

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
def choose_num(arr):
    print("Hey user, give a number to perform binary search:")
    try:
        n = int(input())
        print(Binary_search(arr, n))
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Generate 50 random integers for the array
arr = [random.randint(1, 100) for _ in range(50)]

# Perform MergeSort
sorted_array = mergeSort(arr.copy(), 0, len(arr) - 1)
print("Sorted Array using MergeSort:", sorted_array)

# Choose a number to search in the sorted array
choose_num(sorted_array)


# Complexity-
# time complexity
# Merge Sort	-  O(n log n)	
# Binary Search	- O(log n)  

# space complexity
# Merge Sort	-  O(n)	
# Binary Search	-O(1) (iterative) / O(log n) (recursive)

