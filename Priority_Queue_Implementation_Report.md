
# Deliverables for Priority Queue Implementation and Scheduler Simulation

## 1. Well-Documented Source Code

The priority queue implementation uses a **min-heap** where tasks are stored in a list (array). The following operations are implemented and tested with sample output:

- **Insert (`insert(task)`)**: Inserts tasks into the heap while maintaining the heap property. Example: Task 4 (priority 1) is inserted with tasks 1, 2, and 3.
- **Extract Min (`extract_min()`)**: Removes the task with the highest priority (lowest value) and returns it. Output: 
  ```
  Extracted: 4
  Extracted: 1
  ```
- **Decrease/Increase Key**: Changes a task's priority and adjusts its position. Example: Task 2’s priority is decreased and extracted.
- **Is Empty (`is_empty()`)**: Checks if the queue is empty. Output:
  ```
  Is queue empty? False
  ```

The code is well-commented, explaining each operation and its purpose. The final output shows correct task extraction and queue status.

## 2. Design Choices and Implementation Details

- **Data Structure**: A **list (array)** is used for the binary heap, allowing efficient indexing for parent-child relationships. This simplifies insertion and extraction while maintaining the heap property.
- **Min-Heap**: A **min-heap** was selected, where tasks with the smallest priority are processed first, which is ideal for scheduling tasks based on deadlines or urgency (Cormen et al., 2022, p. 162).
- **Task Class**: The `Task` class stores task attributes like `task_id`, `priority`, `arrival_time`, and `deadline`. The `__lt__` method enables comparison of tasks by priority to maintain the heap order.

## 3. Time Complexity Analysis

- **Insert (`insert(task)`)**: Inserting a new task requires **O(log n)** time due to heapify-up, where `n` is the number of tasks in the queue.
- **Extract Min (`extract_min()`)**: Removing the highest priority task and restoring the heap property with heapify-down takes **O(log n)** time.
- **Decrease/Increase Key**: Adjusting a task’s priority and repositioning it requires **O(log n)** time.
- **Is Empty**: Checking if the queue is empty is a simple operation with **O(1)** time complexity.

The time complexity of each operation ensures that the priority queue performs efficiently even for larger task sets (Cormen et al., 2022, p. 164).

## Citation

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). MIT Press.
