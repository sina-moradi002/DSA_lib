from src.structures.heap.heap import Heap
class Min_Heap(Heap):
    # Private Methods
    def _compare (self, a , b):
        return a < b

    # Override Methods
    def decrease_key(self, index, value):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")

        self.heap[index] -= value
        self._bubble_up(index)

    def increase_key(self, index, value):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")

        self.heap[index] += value
        self._bubble_down(index)