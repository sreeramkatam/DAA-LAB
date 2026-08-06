'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import time

def selection_sort(arr):
    """
    Sorts an array using the Selection Sort algorithm.
    
    TIME COMPLEXITY ANALYSIS:
    🟢 Best Case: O(n²)     - Always scans to confirm minimums.
    🟡 Average Case: O(n²)  - Randomly ordered elements require scanning.
    🔴 Worst Case: O(n²)    - Reverse sorted elements require scanning.
    """
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    print("--- SELECTION SORT DETAILS ---")
    print("🟢 Best Case Complexity:   O(n²)")
    print("🟡 Average Case Complexity:O(n²)")
    print("🔴 Worst Case Complexity:  O(n²)")
    print("------------------------------")
    
    # 📥 Take dynamic user input
    user_input = input("Enter numbers separated by spaces: ")
    # Convert input string into a list of integers
    sample_data = [int(x) for x in user_input.split()]
    
    print(f"\nUnsorted array: {sample_data}")
    
    # ⏱️ Track performance time
    start_time = time.perf_counter()
    selection_sort(sample_data)
    end_time = time.perf_counter()
    
    print(f"Sorted array:   {sample_data}")
    print(f"⏱️ Execution Time: {end_time - start_time:.6f} seconds")
