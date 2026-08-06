from src.structures.heap.heap import Heap
class MaxHeap(Heap):
    # Private methods
    def _bubble_up(self, index):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")
        parent = self.parent(index)
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self.parent(index)

    def _bubble_down(self, index):
        greatest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[greatest]:
            greatest = left
        if right < len(self.heap) and self.heap[right] > self.heap[greatest]:
            greatest = right

        if greatest != index:
            self.heap[index], self.heap[greatest] = self.heap[greatest], self.heap[index]
            self._bubble_down(greatest)

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