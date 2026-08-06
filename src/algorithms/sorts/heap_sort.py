from src.structures.heap.max_heap import MaxHeap

def heap_sort(array):
    # Build heap
    max_heap = MaxHeap()
    for element in array:
        max_heap.insert(element)

    n= max_heap.size()
    for i in range(n - 1, 0, -1):
        max_heap.heap[0], max_heap.heap[i] = max_heap.heap[i], max_heap.heap[0]

        max_heap.heapify(max_heap.heap, i , 0)

    return max_heap.heap
