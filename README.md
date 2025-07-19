# Priority Queue and MaxHeap Implementation in Python

This repository contains two Python files demonstrating custom implementations of a **Max Heap** and a **Priority Queue** using the heap.

## 📂 Files

### 1. `HeapSort.py`
- Implements HeapSort on array of elements

### 2. `MaxHeap.py`
- Implements a **Max Heap** data structure.

### 3. `PriorityQueue.py`
- Implements a **Priority Queue** using the `MaxHeap` class..
- which contain the Task Simulation 

> 📌 Note: The `PriorityQueue.py` file imports and uses the `MaxHeap` class for efficient O(log n) insertions and deletions.

---

## 🧪 Example Usage

```python
# MaxHeap usage
from MaxHeap import MaxHeap

heap = MaxHeap()
heap.insert(10)
heap.insert(5)
heap.insert(20)
print(heap.extract_max())  # Output: 20

```

To run the files
```bash
python run HeapSort.py

python run PriorityQueue.py
```


