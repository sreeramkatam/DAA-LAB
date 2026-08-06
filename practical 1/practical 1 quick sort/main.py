import time
import sys

# Increase recursion depth for worst-case safety on very large arrays
sys.setrecursionlimit(2000)

def quick_sort(arr, low, high):
    """
    Sorts an array using the Quick Sort algorithm (Lomuto partition scheme).
    
    TIME COMPLEXITY ANALYSIS:
    🟢 Best Case: O(n log n)  - Pivot always splits the array into two equal halves.
    🟡 Average Case: O(n log n)- Randomly ordered elements.
    🔴 Worst Case: O(n²)      - Happens if array is already sorted and we pick the 
                                 last element as pivot (unbalanced partitions).
    """
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # Choosing the last element as the pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at i + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == "__main__":
    print("--- QUICK SORT DETAILS ---")
    print("🟢 Best Case Complexity:   O(n log n)")
    print("🟡 Average Case Complexity:O(n log n)")
    print("🔴 Worst Case Complexity:  O(n²)")
    print("----------------------------")
    
    # 📥 Take dynamic user input
    user_input = input("Enter numbers separated by spaces: ")
    sample_data = [int(x) for x in user_input.split()]
    
    print(f"\nUnsorted array: {sample_data}")
    
    # ⏱️ Track performance time
    start_time = time.perf_counter()
    quick_sort(sample_data, 0, len(sample_data) - 1)
    end_time = time.perf_counter()
    
    print(f"Sorted array:   {sample_data}")
    print(f"⏱️ Execution Time: {end_time - start_time:.6f} seconds")
