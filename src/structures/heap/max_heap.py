from src.structures.heap.heap import Heap
class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def _bubble_up(self, index):
        if not index > 1:
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
