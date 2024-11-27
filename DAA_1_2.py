import random


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        left_half = arr[:mid] 
        right_half = arr[mid:]  

       
        merge_sort(left_half)
        merge_sort(right_half)

        
        i = j = k = 0  
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

       
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


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


def main():
   
    arr = random.sample(range(1, 10001), 5000)
    
    print("\nSorting the array using Merge Sort...")
    merge_sort(arr)  
   
    target = int(input("\nEnter the element to search: "))
    
    
    result = binary_search(arr, target)
    print(result)

if __name__ == "__main__":
    main()
