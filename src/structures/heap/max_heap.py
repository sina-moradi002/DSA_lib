from src.structures.heap.heap import Heap
class MaxHeap(Heap):
    # Private methods
    def _compare (self, a , b):
        return a > b

    # Override Methods
    def decrease_key(self, index, value):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")

        self.heap[index] -= value
        self._bubble_down(index)

    def increase_key(self, index, value):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")

        self.heap[index] += value
        self._bubble_up(index)

    def heapify(self, array , n , i):

        # Initialize largest as root
        largest = i

        # left index = 2*i + 1
        l = 2 * i + 1

        # right index = 2*i + 2
        r = 2 * i + 2

        # If left child is larger than root
        if l < n and array[l] > array[largest]:
            largest = l

        # If right child is larger than largest so far
        if r < n and array[r] > array[largest]:
            largest = r

        # If largest is not root
        if largest != i:
            array[i], array[largest] = array[largest], array[i]

            # Recursively heapify the affected sub-tree
            self.heapify(array, n, largest)