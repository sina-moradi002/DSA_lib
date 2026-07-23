from abc import ABC, abstractmethod

class Heap(ABC):
    @abstractmethod
    def __init__(self):
        self.heap = []
        self.nItems = 0

    def insert(self, value):
        self.heap.append(value)
        self.nItems += 1
        self._bubble_up(len(self.heap) - 1)

    def remove(self):
        if not self.nItems > 0:
            return None

        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if self.nItems > 0:
            self.nItems -= 1
            self._bubble_down(0)

        return min_value

    # def decrease_key(self, index, value):
    #     self.heap[index] = self.heap.get(index) - value
    #     self.heapify()
    #
    # def increase_key(self, index, value):
    #     self.heap[index] = self.get(index) + value
    #     self.heapify()

    def get(self, index):
        if not index >= 0:
            raise IndexError("Index out of range")
        return self.heap[index]

    def is_empty(self):
        return self.nItems == 0

    def size(self):
        return self.nItems

    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    def parent(self, index):
        if not index >= 0:
            raise IndexError("Index out of range")
        return (index - 1) // 2

    def left_child(self, index):
        if not index >= 0:
            raise IndexError("Index out of range")
        return 2 * index + 1

    def right_child(self, index):
        if not index >= 0:
            raise IndexError("Index out of range")
        return 2 * index + 2

    @abstractmethod
    def _bubble_up(self, index):
        pass

    @abstractmethod
    def _bubble_down(self):
        pass