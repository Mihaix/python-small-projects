import unittest
import numpy as np
from domain.MyVector import MyVector

class TestMyVector(unittest.TestCase):

    def setUp(self):
        self.vector = MyVector(1, "r", 1, [2, 2, 2])

    def test_add_scalar(self):
        self.vector.add_scalar(3)
        self.assertEqual(self.vector.values, [5, 5, 5])
        self.vector.add_scalar(-2)
        self.assertEqual(self.vector.values, [3, 3, 3])
        self.vector.add_scalar(0)
        self.assertEqual(self.vector.values, [3, 3, 3])

    def test_add(self):
        self.vector.add([1, 1, 1])
        self.assertEqual(self.vector.values, [3, 3, 3])
        self.vector.add([2, 2, 2])
        self.assertEqual(self.vector.values, [5, 5, 5])
        self.vector.add([-1, -1, -1])
        self.assertEqual(self.vector.values, [4, 4, 4])

    def test_subtract(self):
        self.vector.subtract([1, 1, 1])
        self.assertEqual(self.vector.values, [1, 1, 1])
        self.vector.subtract([1, 1, 1])
        self.assertEqual(self.vector.values, [0, 0, 0])
        self.vector.subtract([0, 0, 0])
        self.assertEqual(self.vector.values, [0, 0, 0])

    def test_multiplication(self):
        result = self.vector.multiplication([1, 1, 1])
        self.assertEqual(result, 6)
        result = self.vector.multiplication([2, 2, 2])
        self.assertEqual(result, 12)
        result = self.vector.multiplication([0, 0, 0])
        self.assertEqual(result, 0)

    def test_sum(self):
        result = self.vector.sum()
        self.assertEqual(result, 6)
        self.vector.add_scalar(1)
        result = self.vector.sum()
        self.assertEqual(result, 9)
        self.vector.add_scalar(-3)
        result = self.vector.sum()
        self.assertEqual(result, 0)

    def test_product(self):
        result = self.vector.product()
        self.assertEqual(result, 8)
        self.vector.add_scalar(1)
        result = self.vector.product()
        self.assertEqual(result, 27)
        self.vector.add_scalar(-2)
        result = self.vector.product()
        self.assertEqual(result, 1)

    def test_average(self):
        result = self.vector.average()
        self.assertEqual(result, 2.0)
        self.vector.add_scalar(1)
        result = self.vector.average()
        self.assertEqual(result, 3.0)
        self.vector.add_scalar(-2)
        result = self.vector.average()
        self.assertEqual(result, 1.0)

    def test_minimum(self):
        result = self.vector.minimum()
        self.assertEqual(result, 2)
        self.vector.add_scalar(1)
        result = self.vector.minimum()
        self.assertEqual(result, 3)
        self.vector.add_scalar(-3)
        result = self.vector.minimum()
        self.assertEqual(result, 0)

    def test_maximum(self):
        result = self.vector.maximum()
        self.assertEqual(result, 2)
        self.vector.add_scalar(1)
        result = self.vector.maximum()
        self.assertEqual(result, 3)
        self.vector.add_scalar(-3)
        result = self.vector.maximum()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()