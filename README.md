# MSCS532_Assignment4 (Heap Data Structures: Implementation, Analysis, and Applications)

## How to Run the Code

### Requirements:
- Python 3.x

### Running the Code:
1. Download the source code from the provided `.py` file or copy the provided code.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `.py` file is saved.
4. Run the Python script by typing the following command:
   for windows:
   ``` bash
   python filename.py
   ```
   for MacOS (or Linux):
   ``` bash
   python3 filename.py
   ```
   Replace `<filename>` with the actual name of the Python file.

### File Descriptions

| File Name               | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| [heapsort.py](./heapsort.py)            | Python script implementing the heapsort algorithm.                           |
| [heap_comparison.py](./heap_comparison.py)     | Python script that compares the performance of heapsort, quicksort, and merge sort. |
| [heapsort_analysis.md](./heapsort_analysis.md)   | Report on the heapsort implementation, comparison with other algorithms, and analysis. |
| [priorityQ.py](./priorityQ.py)           | Python script implementing the priority queue using a min-heap.              |
| [Priority_Queue.md](./Priority_Queue.md)      | Contains the detailed report of the priority queue implementation and its operations. |
| [README.md](./README.md)              | This README file with instructions on running the code and summary of findings. |



## Summary of Findings

### Part 1: Heapsort Implementation and Analysis
- **Heapsort** was implemented using a **max-heap** to sort an array. The array was transformed into a max-heap, and then the largest element was repeatedly extracted.
- **Time Complexity**: Heapsort runs in **O(n log n)** in the best, worst, and average cases. It is consistent across input distributions (random, sorted, reverse-sorted), as the heap property needs to be maintained at each step.
- **Space Complexity**: Heapsort is an in-place sorting algorithm, requiring **O(1)** additional space.
- **Comparison**: Heapsort was empirically compared to **Quicksort** and **Merge Sort**. Quicksort showed the best average-case performance but degrades to **O(n²)** in its worst case. Merge Sort performs consistently in **O(n log n)** but uses more space due to its merging step.

### Part 2: Priority Queue Implementation and Applications
- The priority queue was implemented using a **min-heap** structure, which allows efficient insertion, extraction, and priority adjustment of tasks.
- The `Task` class allows the definition of tasks with `task_id`, `priority`, `arrival_time`, and `deadline`.
- **Time complexity** for operations:
- **Insert**: O(log n) using heapify-up.
- **Extract Min**: O(log n) using heapify-down.
- **Decrease/Increase Key**: O(log n) as it adjusts the position of tasks in the heap.
- **Is Empty**: O(1) as it checks if the queue is empty.
- **Design Choices**: A list was chosen for the heap to allow efficient index-based operations, and a `min-heap` was used because it fits task scheduling requirements.
- **Test Output**: Tasks were inserted, extracted by priority, and modified, demonstrating correct priority queue behavior. The final sample output verified the correct extraction and queue status.

## Additional Information

This implementation is suitable for scheduling algorithms where tasks need to be processed based on priority, such as deadline scheduling. It is flexible enough to handle a variety of scheduling policies based on priority values.

## Reference:
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to algorithms (4th ed.). MIT Press.


