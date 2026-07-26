import unittest
from src.structures.heap.max_heap import MaxHeap

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.heap = MaxHeap()

    def test_insert(self):
        self.heap.insert(5)
        self.assertEqual(self.heap.size(), 1)
        self.assertEqual(self.heap.get(0), 5)
        self.heap.insert(10)
        self.assertEqual(self.heap.size(), 2)
        self.assertEqual(self.heap.get(0), 10)
        self.assertEqual(self.heap.get(1), 5)
        self.heap.insert(1)
        self.assertEqual(self.heap.size(), 3)
        self.assertEqual(self.heap.get(0), 10)
        self.assertEqual(self.heap.get(1), 5)
        self.assertEqual(self.heap.get(2), 1)

    def test_remove(self):
        self.assertIsNone(self.heap.remove())
        self.heap.insert(5)
        self.heap.insert(10)
        self.heap.insert(1)
        self.heap.insert(2)
        self.heap.insert(8)
        self.assertEqual(self.heap.size(), 5)
        self.assertEqual(self.heap.get(0), 10)
        self.heap.remove()
        self.assertEqual(self.heap.get(0), 8)
        self.assertEqual(self.heap.get(1), 5)
        self.assertEqual(self.heap.get(2), 1)

    def test_decrease_key(self):
        self.heap.insert(11)
        self.heap.insert(10)
        self.heap.insert(7)
        self.heap.insert(9)
        self.heap.insert(8)
        self.assertEqual(self.heap.size(), 5)
        self.assertEqual(self.heap.get(0), 11)
        self.heap.decrease_key(1 , 5)
        self.assertEqual(self.heap.size(), 5)
        self.assertEqual(self.heap.get(1), 9)
        self.assertEqual(self.heap.get(3), 5)

    def test_increase_key(self):
        self.heap.insert(11)
        self.heap.insert(10)
        self.heap.insert(7)
        self.heap.insert(9)
        self.heap.insert(8)
        self.assertEqual(self.heap.size(), 5)
        self.assertEqual(self.heap.get(0), 11)
        self.heap.increase_key(1 , 2)
        self.assertEqual(self.heap.size(), 5)
        self.assertEqual(self.heap.get(1), 11)
        self.assertEqual(self.heap.get(0), 12)

    def test_is_empty(self):
        self.assertTrue(self.heap.is_empty())
        self.heap.insert(11)
        self.assertFalse(self.heap.is_empty())

    def test_peek(self):
        self.assertIsNone(self.heap.peek())
        self.heap.insert(11)
        self.assertEqual(self.heap.peek(), 11)
        self.heap.insert(7)
        self.assertEqual(self.heap.peek(), 11)
        self.heap.insert(15)
        self.assertEqual(self.heap.peek(), 15)

    def test_parent(self):
        self.assertIsNone(self.heap.parent(0))
        self.heap.insert(11)
        self.assertIsNone(self.heap.parent(0))
        self.heap.insert(7)
        self.assertEqual(self.heap.parent(1), 0)
        self.assertIsNone(self.heap.parent(0))
        self.heap.insert(9)
        self.assertEqual(self.heap.parent(1), 0)
        self.assertEqual(self.heap.parent(2), 0)
        self.assertIsNone(self.heap.parent(0))

    def test_right_child(self):
        self.assertIsNone(self.heap.right_child(0))
        self.heap.insert(11)
        self.assertEqual(self.heap.right_child(0), 2)
        self.heap.insert(7)
        self.assertEqual(self.heap.right_child(0), 2)
        self.assertEqual(self.heap.right_child(1), 4)
        self.heap.insert(9)
        self.assertEqual(self.heap.right_child(0), 2)
        self.assertEqual(self.heap.right_child(1), 4)
        self.assertEqual(self.heap.right_child(2), 6)

    def test_left_child(self):
        self.assertIsNone(self.heap.left_child(0))
        self.heap.insert(11)
        self.assertEqual(self.heap.left_child(0), 1)
        self.heap.insert(7)
        self.assertEqual(self.heap.left_child(0), 1)
        self.assertEqual(self.heap.left_child(1), 3)
        self.heap.insert(9)
        self.assertEqual(self.heap.left_child(0), 1)
        self.assertEqual(self.heap.left_child(1), 3)
        self.assertEqual(self.heap.left_child(2), 5)

if __name__ == '__main__':
    unittest.main()
