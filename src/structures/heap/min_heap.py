from src.structures.heap.heap import Heap
class Min_Heap(Heap):
    # Private Methods
    def _bubble_up(self, index):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")
        parent = self.parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self.parent(index)

    def _bubble_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

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