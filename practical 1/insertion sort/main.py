def insertion_sort(arr):
    # Core Insertion Sort Algorithm
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 1. Take User Input
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# 2. Run the Sorting Algorithm
sorted_numbers = insertion_sort(numbers)

# 3. Print Results and Complexities
print("\n--- RESULTS & COMPLEXITY ---")
print("Sorted Array:", sorted_numbers)
print("\n[TIME COMPLEXITY]")
print("- Best Case:    O(n)   -> Triggered when the input array is already sorted.")
print("- Average Case: O(n²)  -> Triggered when elements are randomly ordered.")
print("- Worst Case:   O(n²)  -> Triggered when the input array is reverse sorted.")
print("\n[SPACE COMPLEXITY]")
print("- Auxiliary Space: O(1) -> Uses constant extra memory because it sorts in-place.")
