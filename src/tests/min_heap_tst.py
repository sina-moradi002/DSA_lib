import unittest
from src.structures.heap.min_heap import Min_Heap

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.heap = Min_Heap()

    def test_insert(self):
        self.heap.insert(5)
        self.assertEqual(self.heap.size, 1)
        self.assertEqual(self.heap.get(0), 5)
        self.heap.insert(10)
        self.assertEqual(self.heap.size, 2)
        self.assertEqual(self.heap.get(0), 5)
        self.assertEqual(self.heap.get(1), 10)
        self.insert(1)
        self.assertEqual(self.heap.size, 3)
        self.assertEqual(self.heap.get(0), 1)
        self.assertEqual(self.heap.get(1), 10)
        self.assertEqual(self.heap.get(2), 5)

    def test_remove(self):
        self.heap.insert(5)
        self.heap.insert(10)
        self.heap.insert(1)
        self.heap.insert(2)
        self.heap.insert(8)
        self.assertEqual(self.heap.size, 5)
        self.assertEqual(self.heap.get(0), 1)
        self.heap.remove()
        self.assertEqual(self.heap.size, 4)
        self.assertEqual(self.heap.get(0), 2)
        self.heap.remove()
        self.assertEqual(self.heap.size, 3)
        self.assertEqual(self.heap.get(0), 5)
        self.assertEqual(self.heap.get(1), 8)
        self.assertEqual(self.heap.get(2), 10)

    def test_decrease_key(self):
        self.heap.insert(11)
        self.heap.insert(10)
        self.heap.insert(7)
        self.heap.insert(9)
        self.heap.insert(8)
        self.assertEqual(self.heap.size, 5)
        self.assertEqual(self.heap.get(0), 7)
        self.heap.decrease_key(3, 7)
        self.assertEqual(self.heap.size, 5)
        self.assertEqual(self.heap.get(0), 4)
        self.assertEqual(self.heap.get(1), 7)
        self.assertEqual(self.heap.get(3), 8)
        self.heap.decrease_key(2 , 2)
        self.assertEqual(self.heap.size, 5)
        self.assertEqual(self.heap.get(0), 4)
        self.assertEqual(self.heap.get(2), 8)

    def test_increase_key(self):
        self.heap.insert(11)
        self.heap.insert(10)
        self.heap.insert(7)
        self.heap.insert(9)
        self.heap.insert(8)
        self.assertEqual(self.heap.size, 5)
        self.assertEqual(self.heap.get(0), 7)
        self.heap.increase_key(1, 7)
        self.assertEqual(self.heap.size, 5)
        self.assertEqual(self.heap.get(0), 4)
        self.assertEqual(self.heap.get(1), 9)
        self.assertEqual(self.heap.get(4), 15)
        self.assertEqual(self.heap.get(3), 11)

    def test_is_empty(self):
        self.assertTrue(self.heap.is_empty())
        self.heap.insert(11)
        self.assertFalse(self.heap.is_empty())

    def test_peek(self):
        self.assertIsNone(self.heap.peek())
        self.heap.insert(11)
        self.assertEqual(self.heap.peek(), 11)
        self.heap.insert(7)
        self.assertEqual(self.heap.peek(), 7)
        self.heap.insert(9)
        self.assertEqual(self.heap.peek(), 7)

    def test_parent(self):
        self.assertIsNone(self.heap.parent(0))
        self.heap.insert(11)
        self.assertIsNone(self.heap.parent(0))
        self.heap.insert(7)
        self.assertEqual(self.heap.parent(1), 11)
        self.assertIsNone(self.heap.parent(0))
        self.heap.insert(9)
        self.assertEqual(self.heap.parent(1), 7)
        self.assertEqual(self.heap.parent(2), 7)
        self.assertIsNone(self.heap.parent(0))

    def test_right_child(self):
        self.assertIsNone(self.heap.right_child(0))
        self.heap.insert(11)
        self.assertIsNone(self.heap.right_child(0))
        self.heap.insert(7)
        self.assertIsNone(self.heap.right_child(0))
        self.heap.insert(9)
        self.assertEqual(self.heap.right_child(0), 9)
        self.assertIsNone(self.heap.right_child(1))
        self.assertIsNone(self.heap.right_child(2))

    def test_left_child(self):
        self.assertIsNone(self.heap.left_child(0))
        self.heap.insert(11)
        self.assertIsNone(self.heap.left_child(0))
        self.heap.insert(7)
        self.assertEqual(self.heap.left_child(0), 11)
        self.heap.insert(9)
        self.assertEqual(self.heap.left_child(0), 11)
        self.assertIsNone(self.heap.left_child(1))
        self.assertIsNone(self.heap.left_child(2))



if __name__ == '__main__':
    unittest.main()
