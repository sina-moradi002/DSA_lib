from src.structures.node import Node

class queue:
    # EXP:  head                           tail
    #       5   -->    6   -->    8   -->     9
    #       size = 4

    # Attributes of queue
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # return True if its empty and return False otherwise
    def is_empty(self):
        return self.size == 0

    # enqueue new data to the queue.
    # FIFO method
    # EXP:  5 -> 6 -> 8 -> 9   ---enqueue(2)-->>  5 -> 6 -> 8 -> 9 -> 2
    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.size = 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1
        return

    # dequeue head node from queue
    # FIFO method
    # EXP: 5 -> 6 -> 8 -> 9 -> 2   ---dequeue()-->>  6 -> 8 -> 9 -> 2
    def dequeue(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def get_head(self):
        return self.head.data