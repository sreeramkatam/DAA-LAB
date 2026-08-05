import time

def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.
    
    TIME COMPLEXITY ANALYSIS:
    🟢 Best Case: O(n log n)   - Divides and merges consistently.
    🟡 Average Case: O(n log n) - Performance remains completely predictable.
    🔴 Worst Case: O(n log n)   - Does not slow down on sorted or reverse data.
    
    SPACE COMPLEXITY: O(n) Auxiliary space (not in-place like Quick Sort).
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Iterators for traversing the two halves and the main list
        i = j = k = 0

        # Copy data to temporary lists left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    print("--- MERGE SORT DETAILS ---")
    print("🟢 Best Case Complexity:   O(n log n)")
    print("🟡 Average Case Complexity:O(n log n)")
    print("🔴 Worst Case Complexity:  O(n log n)")
    print("------------------------------")
    
    # 📥 Take dynamic user input
    user_input = input("Enter numbers separated by spaces: ")
    sample_data = [int(x) for x in user_input.split()]
    
    print(f"\nUnsorted array: {sample_data}")
    
    # ⏱️ Track performance time
    start_time = time.perf_counter()
    merge_sort(sample_data)
    end_time = time.perf_counter()
    
    print(f"Sorted array:   {sample_data}")
    print(f"⏱️ Execution Time: {end_time - start_time:.6f} seconds")
