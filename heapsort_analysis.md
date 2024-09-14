## Analysis of Heapsort Implementation
### Time Complexity:

Heapsort consists of two main phases: building the max-heap and sorting the array by repeatedly extracting the maximum element.

- **Building the Max-Heap** takes O(n) time. This is because the MAX-HEAPIFY operation is applied to each non-leaf node in the array, and while MAX-HEAPIFY takes O(log n) time, its total cost across all nodes sums to O(n) (Cormen et al., 2022, p. 169).
- **Heapify and Extract:** After building the heap, extracting the maximum element n times requires O(log n) per extraction, leading to a time complexity of O(n log n) in the worst, best, and average cases (Cormen et al., 2022, p. 162).

### Space Complexity:

Heapsort is an in-place sorting algorithm, requiring no additional arrays, so its **space complexity is O(1)**. If implemented recursively, the MAX-HEAPIFY function has a stack depth of O(log n), but this can be avoided using iteration (Cormen et al., 2022, p. 165).

Thus, Heapsort achieves O(n log n) time in all cases and has a space complexity of O(1), making it both time- and space-efficient.

## Reference:
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to algorithms (4th ed.). MIT Press.
