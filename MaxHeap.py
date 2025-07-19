
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert a new value into the heap."""
        self.heap.append(value)
        self.heapify(len(self.heap) - 1)

    def extract_max(self):
        """Remove and return the maximum element from the heap."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move last element to root and heapify down
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def parent_index(self, index):
        return (index - 1) // 2
    
    def left_index(self,index):
        return 2 * index + 1
    

    def right_index(self, index):
        return 2 * index + 2

    def heapify(self,index):
        parent_index = self.parent_index(index)

        while index != 0 and self.heap[parent_index] < self.heap[index]:
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = temp

            index = parent_index

            parent_index = self.parent_index(index)

    def heapify_down(self, index):
        """Maintain heap property by shifting down."""
        largest = index
        left = self.left_index(index)
        right = self.right_index(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)

    def peek(self):
        """Return the maximum element without removing it."""
        return self.heap[0] if self.heap else None
    
    def __str__(self):
        return str(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def update_key(self, old_value, new_value):
        if old_value in self.heap:
            index = self.heap.index(old_value)
            self.heap[index] = new_value
            if new_value > old_value:
                self.heapify(index)
            elif new_value < old_value:
                self.heapify_down(index)
        else:
            print(f"Value {old_value} not found in heap.")

if __name__ == "__main__":
    max_heap = MaxHeap()
    for value in [3, 10, 5, 6, 2, 8]:
        max_heap.insert(value)

    print("Heap:", max_heap)

    print("Max element:", max_heap.extract_max())
    print("Heap after extraction:", max_heap)

    max_heap.update_key(5, 12)
    print("Heap after updating 5 to 12:", max_heap)


