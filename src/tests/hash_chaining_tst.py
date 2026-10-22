import unittest
from src.structures.hash.hash_chaining import HashTable

class TestChainingHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(size=7)

    def test_basic_insert_and_search(self):
        self.assertTrue(self.ht.insert(10, "A"))
        self.assertTrue(self.ht.insert(20, "B"))
        self.assertEqual(self.ht.search(10), "A")
        self.assertEqual(self.ht.search(20), "B")
        self.assertIsNone(self.ht.search(99))

    def test_update_existing_key(self):
        self.ht.insert(10, "Value_1")
        
        self.assertFalse(self.ht.insert(10, "Value_2"))
        self.assertEqual(self.ht.search(10), "Value_2")
        
        self.assertEqual(self.ht._HashTable__nItems, 1) 

    def test_delete_and_not_found(self):
        self.ht.insert(15, "X")
        self.assertTrue(self.ht.delete(15))
        self.assertIsNone(self.ht.search(15))
        
        self.assertFalse(self.ht.delete(15))
        self.assertFalse(self.ht.delete(99))

    def test_chaining_collisions(self):
        self.ht.insert(10, "Data_10")
        self.ht.insert(17, "Data_17")
        self.ht.insert(24, "Data_24")

        self.assertEqual(self.ht.search(10), "Data_10")
        self.assertEqual(self.ht.search(17), "Data_17")
        self.assertEqual(self.ht.search(24), "Data_24")
    
        self.assertTrue(self.ht.delete(17))
        self.assertIsNone(self.ht.search(17))
        self.assertEqual(self.ht.search(10), "Data_10")
        self.assertEqual(self.ht.search(24), "Data_24")

    def test_string_keys(self):
        self.ht.insert("Sina", 20)
        self.ht.insert("Mehdi", 19)
        
        self.assertEqual(self.ht.search("Mehdi"), 19)
        self.assertEqual(self.ht.search("Sina"), 20)
        self.assertIsNone(self.ht.search("Ali"))

    def test_dynamic_resizing_and_heavy_load(self):
        for i in range(50):
            self.ht.insert(i, f"Val_{i}")
        
        for i in range(50):
            self.assertEqual(self.ht.search(i), f"Val_{i}")
        self.assertGreater(self.ht.cells(), 7)

if __name__ == '__main__':
    unittest.main()