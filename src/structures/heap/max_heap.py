from src.structures.heap.heap import Heap
class MaxHeap(Heap):
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