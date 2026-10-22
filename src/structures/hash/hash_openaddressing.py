"""
Hash table using open addressing.
Supports linear probing, quadratic probing, and double hashing.
"""


from abc import ABC, abstractmethod

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
    if isinstance(key, int):
        return key

    total = 0
    for char in str(key):
        total = (total * 31) + ord(char)
    return total


# a unique dummy object to mark deleted slots
# we need this so the search doesn't stop when it hits a gap
DELETED = object()

class OpenAddressingHashTable(ABC):
    """Base class for open addressing hash tables"""
    def __init__(self, size=7, hash_func=simpleHash, maxLoadFactor=0.5):
        self._table = [None] * size
        self._nItems = 0
        self._hash_func = hash_func
        self._maxLoadFactor = maxLoadFactor

    def cells(self):
        """Return the total number of slots in the table"""
        return len(self._table)

    def hash(self, key):
        """Get the array index for a key"""
        return self._hash_func(key) % self.cells()

    def loadFactor(self):
        """Calculate the n/m (num of items/num of slots)"""
        return self._nItems / self.cells()

    def _growTable(self):
        """Make the table bigger if it becomes full"""
        oldTable = self._table
        size = len(oldTable) * 2 + 1


        # keep increasing the size until we find a prime number
        # prime sizes help prevent collisions
        while not is_prime(size):
            size += 2

        self._table = [None] * size
        self._nItems = 0

        # move everything from the old table to the new one
        for cell in oldTable:
            if cell is not None and cell is not DELETED:
                self.insert(cell[0], cell[1], check_load=False)

    @abstractmethod
    def probe(self, key, j):
        """Calculate the next index to try. Child classes must implement this"""
        pass

    def insert(self, key, value, check_load=True):
        """nsert a (key, value) pair, handling collisions and deleted slots"""
        first_deleted = None


        # look through the table
        for j in range(self.cells()):
            i = self.probe(key, j)
            cell = self._table[i]

            if cell is None:
                # we found an empty slot
                if first_deleted is not None:
                    # if we saw a deleted spot earlier, use that
                    self._table[first_deleted] = (key, value)
                else:
                    self._table[i] = (key, value)
                
                self._nItems += 1

                # check if we need to grow the table
                if check_load and self._maxLoadFactor < self.loadFactor():
                    self._growTable()
                return True

            elif cell is DELETED:
                # remember the first deleted spot we see
                if first_deleted is None:
                    first_deleted = i
            
            elif cell[0] == key:
                # key already exists, just update the value
                self._table[i] = (key, value)
                return False

        # if the table has no None slots, but has deleted ones, use the first deleted one
        if first_deleted is not None:
            self._table[first_deleted] = (key, value)
            self._nItems += 1
            if check_load and self._maxLoadFactor < self.loadFactor():
                self._growTable()
            return True
            
        raise Exception("Hash table is completely full!")

    def search(self, key):
        """Find a value by its key"""
        for j in range(self.cells()):
            i = self.probe(key, j)
            cell = self._table[i]
            
            if cell is None:
                return None
            elif cell is DELETED:
                pass 
            elif cell[0] == key:
                return cell[1]
                
        return None

    def delete(self, key):
        """Mark a slot as deleted"""
        for j in range(self.cells()):
            i = self.probe(key, j)
            cell = self._table[i]
            
            if cell is None:
                return False
            elif cell is DELETED:
                pass 
            elif cell[0] == key:
                self._table[i] = DELETED
                self._nItems -= 1
                return True
                
        return False


class LinearProbing(OpenAddressingHashTable):
    """Linear probing: try the very next slot (i+1, i+2, etc)"""
    def probe(self, key, j):
        start_index = self.hash(key)
        return (start_index + j) % self.cells()


class QuadraticProbing(OpenAddressingHashTable):
    """Quadratic probing: jump in increasing steps (i+1, i+4, i+9, etc)"""
    def __init__(self, size=7, hash_func=simpleHash, maxLoadFactor=0.5, c1=0, c2=1):
        super().__init__(size, hash_func, maxLoadFactor)
        self.c1 = c1
        self.c2 = c2

    def probe(self, key, j):
        start_index = self.hash(key)
        return (start_index + self.c1 * j + self.c2 * (j ** 2)) % self.cells()


class DoubleHashing(OpenAddressingHashTable):
    """Double hashing: use a second hash function to calculate the jump size"""
    def __init__(self, size=7, hash_func=simpleHash, maxLoadFactor=0.5, R=5):
        super().__init__(size, hash_func, maxLoadFactor)
        self.R = R

    def hash2(self, key):
        """The second hash function used for step size"""
        numeric_key = self._hash_func(key)
        return self.R - (numeric_key % self.R)

    def probe(self, key, j):
        start_index = self.hash(key)
        step_size = self.hash2(key)
        return (start_index + (j * step_size)) % self.cells()
