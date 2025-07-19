import random
import time

from HeapSort import heapsort

# for more testing purposes
import sys
sys.setrecursionlimit(10000)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def time_algorithm(algorithm, arr):
    start = time.time()
    if algorithm.__name__ == 'heapsort':
        algorithm(arr)  
    else:
        algorithm(arr)  
    return time.time() - start


def compare_algorithms():
    input_sizes = [100, 1000]
    input_types = ['Random', 'Sorted', 'Reversed']

    algorithms = {
        "Heapsort": heapsort,
        "Quicksort": quicksort,
        "Merge Sort": merge_sort
    }

    for size in input_sizes:
        print(f"\n=== Input Size: {size} ===")
        original = [random.randint(1, size) for _ in range(size)]

        for data_type in input_types:
            if data_type == 'Random':
                data = original.copy()
            elif data_type == 'Sorted':
                data = sorted(original)
            elif data_type == 'Reversed':
                data = sorted(original, reverse=True)

            print(f"\n--- {data_type} Input ---")
            for name, algo in algorithms.items():
                arr_copy = data.copy()
                elapsed = time_algorithm(algo, arr_copy)
                print(f"{name:10s}: {elapsed:.6f} sec")

# Run the comparison
compare_algorithms()


