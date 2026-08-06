import time

def heapify(arr, n, i):
    """
    Turns a subtree rooted at index i into a Max-Heap.
    n is the total size of the heap.
    """
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root, swap them
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a Max-Heap from the input list
    # We start from the last non-leaf node and go backwards to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move the current root (largest element) to the end of the array
        arr[0], arr[i] = arr[i], arr[0]
        
        # Call max heapify on the reduced heap to restore heap property
        heapify(arr, i, 0)

# Get user input for the list
user_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(f"Original list: {user_list}")

# Measure execution time
start_time = time.perf_counter()
heap_sort(user_list)
end_time = time.perf_counter()

# Output results
print(f"Sorted list:   {user_list}")
print(f"Execution time: {(end_time - start_time):.8f} seconds")
