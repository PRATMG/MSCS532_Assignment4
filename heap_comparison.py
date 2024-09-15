# This code compares the running times of three sorting algorithms: Heapsort, Quicksort, and Merge Sort.
# It measures the performance of these algorithms on different input sizes and distributions
# (sorted, reverse-sorted, and random arrays). The running time for each algorithm is recorded
# and printed in a clean, tabular format for easy readability.

import time
import random

# Heapsort (as implemented earlier)
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heapsort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

# Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Utility function to test sorting algorithms and format the output
def test_sorting_algorithms(sizes, distributions):
    print(f"{'Array Size':<10} {'Distribution':<15} {'Heapsort (sec)':<15} {'Quicksort (sec)':<15} {'Merge Sort (sec)':<15}")
    print("-" * 70)

    for size in sizes:
        for dist_name, dist in distributions.items():
            arr = dist(size)
            
            # Heapsort
            arr_copy = arr[:]
            start_time = time.time()
            heapsort(arr_copy)
            heapsort_time = time.time() - start_time
            
            # Quicksort
            arr_copy = arr[:]
            start_time = time.time()
            quicksort(arr_copy)
            quicksort_time = time.time() - start_time
            
            # Merge Sort
            arr_copy = arr[:]
            start_time = time.time()
            merge_sort(arr_copy)
            mergesort_time = time.time() - start_time
            
            print(f"{size:<10} {dist_name:<15} {heapsort_time:<15.6f} {quicksort_time:<15.6f} {mergesort_time:<15.6f}")

# Distributions: sorted, reverse-sorted, random
distributions = {
    "Sorted": lambda size: list(range(size)),
    "Reverse-Sorted": lambda size: list(range(size, 0, -1)),
    "Random": lambda size: [random.randint(1, size) for _ in range(size)]
}

# Input sizes to test (smaller sizes for better execution times)
sizes = [100, 200, 500, 1000, 2000]

# Run the tests
test_sorting_algorithms(sizes, distributions)
