import time

def bubble_sort(arr):
    """
    Sorts an array using the optimized Bubble Sort algorithm.
    
    TIME COMPLEXITY ANALYSIS:
    🟢 Best Case: O(n)     - Array is already sorted. Breaks early.
    🟡 Average Case: O(n²)  - Randomly ordered elements.
    🔴 Worst Case: O(n²)    - Reverse sorted elements.
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # Best case exit trigger
        if not swapped:
            break

if __name__ == "__main__":
    print("--- BUBBLE SORT DETAILS ---")
    print("🟢 Best Case Complexity:   O(n)")
    print("🟡 Average Case Complexity:O(n²)")
    print("🔴 Worst Case Complexity:  O(n²)")
    print("----------------------------")
    
    # 📥 Take dynamic user input
    user_input = input("Enter numbers separated by spaces: ")
    # Convert input string into a list of integers
    sample_data = [int(x) for x in user_input.split()]
    
    print(f"\nUnsorted array: {sample_data}")
    
    # ⏱️ Track performance time
    start_time = time.perf_counter()
    bubble_sort(sample_data)
    end_time = time.perf_counter()
    
    print(f"Sorted array:   {sample_data}")
    print(f"⏱️ Execution Time: {end_time - start_time:.6f} seconds")
