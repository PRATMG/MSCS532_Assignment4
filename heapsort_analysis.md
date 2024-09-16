## Analysis of Heapsort Implementation

### 1. Implementation
Heapsort algorithm is implemented [here](./heapsort.py)  

### 2. Analysis of Implementation

#### Time Complexity:
Heapsort consists of two main phases: building the max-heap and sorting the array by repeatedly extracting the maximum element.

- **Building the Max-Heap** takes O(n) time. This is because the MAX-HEAPIFY operation is applied to each non-leaf node in the array, and while MAX-HEAPIFY takes O(log n) time, its total cost across all nodes sums to O(n) (Cormen et al., 2022, p. 169).
- **Heapify and Extract:** After building the heap, extracting the maximum element n times requires O(log n) per extraction, leading to a time complexity of O(n log n) in the worst, best, and average cases (Cormen et al., 2022, p. 162).

#### Space Complexity:
Heapsort is an in-place sorting algorithm, requiring no additional arrays, so its **space complexity is O(1)**. If implemented recursively, the MAX-HEAPIFY function has a stack depth of O(log n), but this can be avoided using iteration (Cormen et al., 2022, p. 165).

Thus, Heapsort achieves O(n log n) time in all cases and has a space complexity of O(1), making it both time- and space-efficient.

### 3. Comparison
Output of the code:

| Array Size | Distribution    | Heapsort (sec) | Quicksort (sec) | Merge Sort (sec) |
|------------|-----------------|----------------|-----------------|------------------|
| 500        | Sorted          | 0.003802       | 0.000938        | 0.001996         |
| 500        | Reverse-Sorted  | 0.003291       | 0.001116        | 0.001619         |
| 500        | Random          | 0.002910       | 0.001137        | 0.002579         |
| 1000       | Sorted          | 0.007145       | 0.002093        | 0.003789         |
| 1000       | Reverse-Sorted  | 0.006206       | 0.001935        | 0.003848         |
| 1000       | Random          | 0.059391       | 0.002427        | 0.004802         |
| 2000       | Sorted          | 0.098678       | 0.016000        | 0.013876         |
| 2000       | Reverse-Sorted  | 0.083373       | 0.008186        | 0.073593         |
| 2000       | Random          | 0.030284       | 0.073587        | 0.024347         |
| 4000       | Sorted          | 0.171411       | 0.016349        | 0.083721         |
| 4000       | Reverse-Sorted  | 0.116024       | 0.016815        | 0.089558         |
| 4000       | Random          | 0.261971       | 0.019677        | 0.113648         |
| 6000       | Sorted          | 0.192105       | 0.086628        | 0.097911         |
| 6000       | Reverse-Sorted  | 0.203165       | 0.094861        | 0.096825         |
| 6000       | Random          | 0.225308       | 0.039876        | 0.110356         |

#### Discussion of Observed Results and Theoretical Analysis

- **Heapsort:**  
Heapsort performed consistently across all input distributions and sizes, maintaining its expected O(n log n) time complexity. As input size increased, Heapsort's performance slowed, particularly with larger random inputs (e.g., 0.261971 sec for 4000 elements). This behavior aligns with its need to maintain the max-heap property, which takes O(log n) operations per element (Cormen et al., 2022, p. 162).

- **Quicksort:**  
Quicksort was the fastest algorithm for small to medium input sizes. For example, with 500 elements, Quicksort sorted random arrays in 0.001137 sec, outperforming Heapsort. However, with larger arrays, especially random inputs, Quicksort's performance degraded (e.g., 0.073587 sec for 2000 elements). This is consistent with its O(n log n) average-case complexity and potential O(n²) worst case when poor pivots are selected (Cormen et al., 2022, p. 171).

- **Merge Sort:**  
Merge Sort showed stable performance across all distributions, as expected with its O(n log n) time complexity. However, for larger arrays, it was slower than Quicksort and Heapsort due to the overhead of merging and additional space requirements (e.g., 0.110356 sec for 6000 random elements) (Cormen et al., 2022, p. 177).

### Conclusion
Quicksort is typically the fastest for smaller arrays, while Heapsort is consistent across input types and sizes. Merge Sort, though stable, incurs higher space and merging overheads. These results align well with their theoretical time complexities.

## Reference:
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). MIT Press.
