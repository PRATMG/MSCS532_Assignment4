def max_heapify(arr, n, i):
    """
    Ensure the subtree rooted at index i follows the max-heap property.
    :param arr: List representing the heap.
    :param n: Total size of the heap.
    :param i: Index of the root of the subtree.
    """
    largest = i        # Initialize largest as root
    left = 2 * i + 1   # Left child index
    right = 2 * i + 2  # Right child index

    # If left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected subtree
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    """
    Build a max-heap from the unsorted array.
    :param arr: List representing the array to transform into a heap.
    """
    n = len(arr)
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heapsort(arr):
    """
    Perform heapsort on the given array.
    :param arr: List to be sorted.
    """
    n = len(arr)

    # Step 1: Build a max-heap
    build_max_heap(arr)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move the current root (maximum) to the end
        arr[i], arr[0] = arr[0], arr[i]
        # Call max_heapify on the reduced heap
        max_heapify(arr, i, 0)

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Unsorted array:", arr)
    heapsort(arr)
    print("Sorted array:", arr)
