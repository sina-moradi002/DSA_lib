from abc import ABC, abstractmethod

class Heap(ABC):
    @abstractmethod
    def __init__(self):
        self.heap = []
        self.nItems = 0

    def insert(self, value):
        self.heap.append(value)
        self.nItems += 1
        pass

    def remove(self):
        pass

    def decrease_key(self, index,value):
        pass

    def increase_key(self, index, value):
        pass

    def get(self, index):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

    def peek(self):
        pass

    def parent(self, index):
        pass

    def left_child(self, index):
        pass

    def right_child(self, index):
        pass

    @abstractmethod
    def heapify(self):
        pass