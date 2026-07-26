from abc import ABC, abstractmethod

class Heap(ABC):
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def remove(self):
        if self.is_empty():
            return None

        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._bubble_down(0)

        return root

    # def decrease_key(self, index, value):
    #     self.heap[index] = self.heap.get(index) - value
    #     self.heapify()
    #
    # def increase_key(self, index, value):
    #     self.heap[index] = self.get(index) + value
    #     self.heapify()

    def get(self, index):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")
        return self.heap[index]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def parent(self, index):
        if self.is_empty():
            return None
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")
        if index == 0:
            return None
        return (index - 1) // 2

    def left_child(self, index):
        if self.is_empty():
            return None

        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")

        return 2 * index + 1

    def right_child(self, index):
        if self.is_empty():
            return None

        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")

        return 2 * index + 2

    @abstractmethod
    def _bubble_up(self, index):
        pass

    @abstractmethod
    def _bubble_down(self, index):
        pass