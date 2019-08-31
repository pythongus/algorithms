"""
Unit Test For Heaps
"""
import unittest
from algo.heap import create_heap


class TestHeap(unittest.TestCase):

    def test_create_heap_empty_list(self):
        self.assertIsNone(create_heap([]))

    def test_create_heap_ascending_values(self):
        values = [1, 2, 3, 19, 35, 100]
        root = create_heap(values)
        self.assertEqual(root["value"], 100)

    def test_create_heap_descending_values(self):
        values = [100, 35, 19]
        root = create_heap(values)
        self.assertEqual(root["value"], 100)
        self.assertEqual(root["left"]["value"], 35)
        self.assertEqual(root["right"]["value"], 19)

    def test_create_heap_varying_1(self):
        values = [100, 35, 19, 101]
        root = create_heap(values)
        self.assertEqual(root["value"], 101)
        self.assertEqual(root["left"]["value"], 100)
        self.assertIsNone(root["right"])

    def test_create_heap_varying_2(self):
        values = [100, 35, 19, 101, 12]
        root = create_heap(values)
        self.assertEqual(root["value"], 101)
        self.assertEqual(root["left"]["value"], 100)
        self.assertEqual(root["right"]["value"], 12)

    def test_create_heap_varying_3(self):
        values = [100, 35, 19, 101, 12, 55]
        root = create_heap(values)
        self.assertEqual(root["value"], 101)
        self.assertEqual(root["left"]["value"], 100)
        self.assertEqual(root["right"]["value"], 12)

    def test_create_heap_varying_4(self):
        values = [100, 35, 19, 101, 12, 55, 102, 11, 1, 7, 8]
        root = create_heap(values)
        self.assertEqual(root["value"], 102)
        self.assertEqual(root["left"]["value"], 101)
        self.assertEqual(root["right"]["value"], 11)

    def test_create_heap_varying_5(self):
        values = [1, 35, 19, 11, 12, 55, 2, 11, 1, 7, 8]
        root = create_heap(values)
        self.assertEqual(root["value"], 55)
        self.assertEqual(root["left"]["value"], 35)
        self.assertEqual(root["right"]["value"], 2)

    def test_create_heap_varying_6(self):
        values = [1, 3, 10, 9, 8, 12, 2, 2, 2, 1, 100]
        root = create_heap(values)
        self.assertEqual(root["value"], 100)

    def test_create_heap_varying_7(self):
        values = [10, 3, 1, 4, 2]
        root = create_heap(values)
        self.assertEqual(root["value"], 10)
        self.assertEqual(root["left"]["value"], 4)
        self.assertEqual(root["right"]["value"], 1)


if __name__ == "__main__":
    unittest.main()
