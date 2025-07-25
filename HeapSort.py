def heapify(arr, n, i):
    """Maintain max-heap property."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left

    
    if right < n and arr[right] > arr[largest]:
        largest = right

    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    """Heapsort implementation."""
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)

    return arr

arr = [9, 4, 3, 8, 10, 2, 5] 
heapsort(arr)
print(arr)
