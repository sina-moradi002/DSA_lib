import unittest
from src.structures.hash.hash_openaddressing import LinearProbing, QuadraticProbing, DoubleHashing

class TestOpenAddressingHashTable(unittest.TestCase):
    def setUp(self):
        self.ht_linear = LinearProbing(size=7)
        self.ht_quadratic = QuadraticProbing(size=7)
        self.ht_double = DoubleHashing(size=7)
        self.tables = [self.ht_linear, self.ht_quadratic, self.ht_double]

    def test_basic_insert_and_search(self):
        for ht in self.tables:
            self.assertTrue(ht.insert(10, "A"))
            self.assertTrue(ht.insert(20, "B"))
            self.assertEqual(ht.search(10), "A")
            self.assertEqual(ht.search(20), "B")
            self.assertIsNone(ht.search(99))

    def test_update_existing_key(self):
        for ht in self.tables:
            ht.insert(10, "Value_1")

            self.assertFalse(ht.insert(10, "Value_2"))
            self.assertEqual(ht.search(10), "Value_2")

            self.assertEqual(ht._nItems, 1)

    def test_delete_and_not_found(self):
        for ht in self.tables:
            ht.insert(15, "X")
            self.assertTrue(ht.delete(15))
            self.assertIsNone(ht.search(15))
            
            self.assertFalse(ht.delete(15))
            self.assertFalse(ht.delete(99))

    def test_search_after_deletion(self):
        for ht in self.tables:
            ht.insert(10, "Data10")
            ht.insert(17, "Data17")
            ht.insert(24, "Data24")

            ht.delete(17)
            
            self.assertEqual(ht.search(24), "Data24")
            self.assertIsNone(ht.search(17))

    def test_string_keys(self):
        for ht in self.tables:
            ht.insert("Sina", 20)
            ht.insert("Mehdi", 19)
            ht.insert("Willy", 18)
            
            self.assertEqual(ht.search("Mehdi"), 19)
            self.assertEqual(ht.search("Sina"), 20)
            self.assertIsNone(ht.search("Ali"))

    def test_dynamic_resizing_and_heavy_load(self):
        for ht in self.tables:
            for i in range(50):
                ht.insert(i, f"Val_{i}")
            
            for i in range(50):
                self.assertEqual(ht.search(i), f"Val_{i}")
            
            self.assertGreater(ht.cells(), 7)

    def test_load_factor_accuracy(self):
        for ht in self.tables:
            self.assertEqual(ht.loadFactor(), 0.0)
            ht.insert(1, "A")
            ht.insert(2, "B")
            self.assertAlmostEqual(ht.loadFactor(), 2/7)

if __name__ == '__main__':
    unittest.main()
