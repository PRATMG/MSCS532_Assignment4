# Part A: Priority Queue Implementation
# This file implements a priority queue using a binary heap (min-heap) with task scheduling.
# It includes task insertion, extraction, priority adjustment, and a check if the queue is empty.
# All functions are documented with their purpose and time complexity.

class Task:
    """
    Task class to represent a task with ID, priority, arrival time, and deadline.
    The priority is used for heap ordering.
    """
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority  # Lower values represent higher priority in a min-heap
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        """
        Comparison operator to maintain heap property in a min-heap.
        Task with smaller priority value has higher priority.
        """
        return self.priority < other.priority


class PriorityQueue:
    """
    PriorityQueue class implemented as a binary min-heap.
    It supports insert, extract_min, increase/decrease_key, and is_empty operations.
    """
    def __init__(self):
        self.heap = []  # The heap is represented as a list (array-based binary heap)

    # Inserts a new task into the heap while maintaining the heap property.
    def insert(self, task):
        self.heap.append(task)  # Add the task at the end
        self._heapify_up(len(self.heap) - 1)  # Adjust heap using heapify-up

    def _heapify_up(self, index):
        """
        Heapify-up operation to restore the heap property after insertion.
        Moves the task upwards if its priority is smaller than its parent.
        """
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            # Swap with parent if the task has a higher priority (lower value)
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    # Extracts and returns the task with the highest priority (smallest priority value).
    def extract_min(self):
        if len(self.heap) == 0:
            return None  # The heap is empty
        min_task = self.heap[0]  # The root is the minimum element
        self.heap[0] = self.heap.pop()  # Replace root with the last element
        self._heapify_down(0)  # Restore heap property using heapify-down
        return min_task


    """
    Heapify-down operation to restore the heap property after extraction.
    Moves the task downwards if its priority is greater than its children.
    """
    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        # Find the smallest among root, left child, and right child
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        
        # If the smallest isn't the root, swap and continue heapify-down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

  # Decreases the priority of a task at a given index and adjusts its position in the heap.
    def decrease_key(self, index, new_priority):
        if new_priority >= self.heap[index].priority:
            return  # New priority must be smaller for decrease_key
        self.heap[index].priority = new_priority
        self._heapify_up(index)

    def increase_key(self, index, new_priority):
        """
        Increases the priority of a task at a given index and adjusts its position in the heap.
        """
        if new_priority <= self.heap[index].priority:
            return  # New priority must be larger for increase_key
        self.heap[index].priority = new_priority
        self._heapify_down(index)


    # Returns True if the priority queue is empty, False otherwise.
    def is_empty(self):
        """
        """
        return len(self.heap) == 0

if __name__ == "__main__":
    # Initialize a priority queue
    pq = PriorityQueue()

    # Create some tasks with different priorities
    task1 = Task(task_id=1, priority=5, arrival_time=0, deadline=10)
    task2 = Task(task_id=2, priority=3, arrival_time=1, deadline=15)
    task3 = Task(task_id=3, priority=4, arrival_time=2, deadline=20)
    task4 = Task(task_id=4, priority=1, arrival_time=3, deadline=25)

    # Insert tasks into the priority queue
    pq.insert(task1)
    pq.insert(task2)
    pq.insert(task3)
    pq.insert(task4)

    # Extract the task with the highest priority (lowest priority value)
    print("Extracted:", pq.extract_min().task_id)  # Should extract task with ID 4 (priority 1)

    # Decrease the priority of a task and adjust its position
    pq.decrease_key(1, 0)  # Decrease task2's priority to 0
    print("Extracted:", pq.extract_min().task_id)  # Should extract task with ID 2 (new priority 0)

    # Check if the queue is empty
    print("Is queue empty?", pq.is_empty())  # Should return False
