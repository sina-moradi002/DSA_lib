import unittest
from src.structures.trees.bst import BinarySearchTree


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

    def test_insert(self):
        self.tree.insert(5)
        self.assertEqual(self.tree.root.data, 5)
        self.assertEqual(self.tree.root.left, None)
        self.assertEqual(self.tree.root.right, None)
        self.assertEqual(self.tree.get_size(), 1)
        self.tree.insert(7)
        self.assertEqual(self.tree.root.left, None)
        self.assertEqual(self.tree.root.right.data, 7)
        self.assertEqual(self.tree.root.right.left, None)
        self.assertEqual(self.tree.root.right.right, None)
        self.assertEqual(self.tree.get_size(), 2)
        self.tree.insert(6)
        self.assertEqual(self.tree.root.right.left.data, 6)

    def test_is_empty(self):
        self.assertTrue(self.tree.is_empty())
        self.tree.insert(5)
        self.assertFalse(self.tree.is_empty())

    def test_size(self):
        self.assertEqual(self.tree.get_size(), 0)
        self.tree.insert(6)
        self.assertEqual(self.tree.get_size(), 1)

    def test_height(self):
        self.assertEqual(self.tree.get_hight(), -1)
        self.tree.insert(5)
        self.assertEqual(self.tree.get_hight(), 0)
        self.tree.insert(6)
        self.tree.insert(4)
        self.tree.insert(3)
        self.assertEqual(self.tree.get_hight(), 2)

    def test_preorder(self):
        self.assertEqual(self.tree.preorder(), [])
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(9)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(3)
        self.assertEqual(self.tree.preorder(), [5, 4, 2, 3, 9, 7])

    def test_inorder(self):
        self.assertEqual(self.tree.inorder(), [])
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(9)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(3)
        self.assertEqual(self.tree.inorder(), [2, 3, 4, 5, 7, 9])

    def test_postorder(self):
        self.assertEqual(self.tree.postorder(), [])
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(9)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(3)
        self.assertEqual(self.tree.postorder(), [3, 2, 4, 7, 9, 5])

    def test_search(self):
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(9)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(3)
        self.assertTrue(self.tree.search(2))
        self.assertFalse(self.tree.search(15))

    def test_find_max(self):
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(9)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(3)
        self.assertEqual(self.tree.find_max(), 9)

    def test_find_min(self):
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(9)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(3)
        self.assertEqual(self.tree.find_min(), 2)

    def test_delete(self):
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(9)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(3)
        self.tree.delete(3)
        self.assertEqual(self.tree.postorder(), [2, 4, 7, 9, 5])
        self.tree.delete(4)
        self.assertEqual(self.tree.postorder(), [2, 7, 9, 5])


if __name__ == '__main__':
    unittest.main()
