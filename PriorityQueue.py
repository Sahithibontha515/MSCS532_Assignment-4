
from MaxHeap import MaxHeap
import time
class Task:
    def __init__(self, task, priority, arrival_time, deadline):
        self.priority = priority
        self.task = task
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __gt__(self ,other):
        return self.priority > other.priority

    def __repr__(self):
        return f"Task(ID={self.task}, Priority={self.priority}, Arrival={self.arrival_time}, Deadline={self.deadline})"



def simulate_task_scheduler(tasks):
    pq = MaxHeap()
    current_time = 0
    completed_tasks = []

    for task in tasks:
        pq.insert(task)

    while not pq.is_empty():
        task = pq.extract_max()
        current_time += 1  # Simulate time passage
        print(f"Executing {task} at time {current_time}")
        completed_tasks.append((task.task, current_time))

    return completed_tasks

if __name__ == "__main__":
    # Example Task list
    tasks = [
        Task("T1", 3, 0, 10),
        Task("T2", 1, 1, 5),
        Task("T3", 2, 2, 8),
        Task("T4", 4, 3, 12)
    ]

    results = simulate_task_scheduler(tasks)
    print("\nCompleted Tasks (ID, Completion Time):")
    for res in results:
        print(res)
    