from abc import ABC, abstractmethod

# This structure is a heap is a tree-based data structure that satisfies the heap property:
# In a max heap, for any given node C, if P is the parent node of C, then the key (the value)
# of P is greater than or equal to the key of C.
# In a min heap, the key of P is less than or equal to the key of C.
# The node at the "top" of the heap (with no parents) is called the root node. It's always the Maximum/Minimum of the heap
# Heap actually is a list; so any access to any element of it cost O(1) time.
# It used in heap sort too!

class Heap(ABC):
    def __init__(self):
        self.heap = []
    # Normal Methods:

    # Insert a new element
    def insert(self, value):
        # append it to the list
        self.heap.append(value)
        # configure heap property
        self._bubble_up(len(self.heap) - 1)

    # Remove the top element of the heap (index = 0)
    def remove(self):
        # return None if its empty
        if self.is_empty():
            return None

        # swap first and last elements
        root = self.heap[0]
        last = self.heap.pop()

        # configure heap property
        if self.heap:
            self.heap[0] = last
            self._bubble_down(0)

        # return removed element
        return root

    # This method returns amount of given index if its exists
    def get(self, index):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")
        return self.heap[index]

    # This method returns True if heap is empty and False otherwise
    def is_empty(self):
        return len(self.heap) == 0

    # returns length of vector
    def size(self):
        return len(self.heap)

    # This method returns the root of the heap which is the Maximum/Minimum element
    def peek(self):
        # returns None if its empty
        if self.is_empty():
            return None
        return self.heap[0]

    # This method returns index of parent of the given index
    # for actual value use get() method. EXP: get(parent(index))
    def parent(self, index):
        # returns None if its empty
        if self.is_empty():
            return None

        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")

        # Root have not parent
        if index == 0:
            return None
        return (index - 1) // 2

    # This method returns index of parent of the given index
    # for actual value use get() method. EXP: get(parent(index))
    def left_child(self, index):
        # returns None if its empty
        if self.is_empty():
            return None

        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")

        return 2 * index + 1

    # This method returns index of parent of the given index
    # for actual value use get() method. EXP: get(parent(index))
    def right_child(self, index):
        # returns None if its empty
        if self.is_empty():
            return None

        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")

        return 2 * index + 2

    # Abstract Methods:
    @abstractmethod
    def _bubble_up(self, index):
        pass

    @abstractmethod
    def _bubble_down(self, index):
        pass

    @abstractmethod
    def decrease_key(self, index, value):
        pass

    @abstractmethod
    def increase_key(self, index, value):
        pass