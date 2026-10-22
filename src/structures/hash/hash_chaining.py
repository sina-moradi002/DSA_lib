"""
Hash table using separate chaining.
We use linked lists to handle collisions (when two keys get the same index).
"""


def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def simpleHash(key):
    """Convert a string or int key to a hash number"""

    # if it is already an int, we don't need to do anything
    if isinstance(key, int):
        return key

    # hash strings: multiply by 31 and add the char code
    total = 0
    for char in str(key):
        total = (total * 31) + ord(char)
    return total


class Node:
    """A node for linked list"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class KeyValueList:
    """A custom linked list to store items inside the hash table slots"""
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        """Add a new item or update the key if it is already added"""
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return False
            current = current.next

        # when the key is new, we put it at the start (head) of the list :)
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        return True

    def search(self, key):
        """Search a key in a list and return its value"""
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        """Find the key and remove its node from the list"""
        current = self.head
        previous = None
        while current is not None:
            if current.key == key:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def traverse(self):
        """Get all items in the list"""
        items = []
        current = self.head
        while current is not None:
            items.append((current.key, current.value))
            current = current.next
        return items


class HashTable:
    """The main hash table class"""
    def __init__(self, size=7, hash_func=simpleHash, maxLoadFactor=0.5):
        self.__table = [None] * size
        self.__nItems = 0
        self.__hash = hash_func
        self.__maxLoadFactor = maxLoadFactor

    def cells(self):
        """Return the total number of slots in the table"""
        return len(self.__table)

    def hash(self, key):
        """Get the array index for a key"""
        return self.__hash(key) % self.cells()

    def loadFactor(self):
        """Calculate the n/m (num of items/num of slots)"""
        return self.__nItems / self.cells()

    def __growTable(self):
        """Make the table bigger if it becomes full"""
        oldTable = self.__table
        size = len(oldTable) * 2 + 1

        # keep increasing the size until we find a prime number
        # prime sizes help prevent collisions
        while not is_prime(size):
            size += 2

        self.__table = [None] * size
        self.__nItems = 0

        # move everything from the old table to the new one
        for i in range(len(oldTable)):
            if oldTable[i] is not None:
                for key, value in oldTable[i].traverse():
                    self.insert(key, value, check_load=False)

    def insert(self, key, value, check_load=True):
        """Insert a pair of (key, value) to the table"""
        i = self.hash(key)

        # if the slot is completely empty, put a new linked list there first
        if self.__table[i] is None:
            self.__table[i] = KeyValueList()
        is_inserted = self.__table[i].insert(key, value)

        if is_inserted:
            self.__nItems += 1

        # if the table is getting too full, make it bigger
        # check_load acts like a switch so we can turn this off during __growTable
        if check_load and self.__maxLoadFactor < self.loadFactor():
            self.__growTable()

        return is_inserted

    def search(self, key):
        """Find a value with its key"""
        i = self.hash(key)
        return None if self.__table[i] is None else self.__table[i].search(key)

    def delete(self, key):
        """Remove a key from the table"""
        i = self.hash(key)

        if self.__table[i] is None:
            return False

        is_deleted = self.__table[i].delete(key)

        if is_deleted:
            self.__nItems -= 1

        return is_deleted
