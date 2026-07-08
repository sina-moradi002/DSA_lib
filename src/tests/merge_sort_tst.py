import unittest
from src.algorithms.sorts.merge import merge_sort


class InsertionSortTest(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        result = merge_sort(arr)
        self.assertEqual(result, [])

    def test_one_element(self):
        arr = [13]
        result = merge_sort(arr)
        self.assertEqual(result, [13])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_duplicate_sorted(self):
        arr = [1, 1, 2, 3, 3, 4, 4, 4, 5]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 1, 2, 3, 3, 4, 4, 4, 5])

    def test_normal_unsorted(self):
        arr = [4, 3, 2, 5, 6, 1]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_duplicates_unsorted(self):
        arr = [3, 5, 6, 2, 1, 3, 2, 5, 3, 6]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 2, 2, 3, 3, 3, 5, 5, 6, 6])

    def test_descending_array(self):
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = merge_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
