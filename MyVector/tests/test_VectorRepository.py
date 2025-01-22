import unittest
from domain.MyVector import MyVector
from repo.VectorRepository import VectorRepository

class TestVectorRepository(unittest.TestCase):

    def setUp(self):
        self.repo = VectorRepository([
            MyVector(1, "r", 1, [2, 2, 2]),
            MyVector(2, "b", 2, [4, 0, 1]),
            MyVector(3, "g", 3, [7, 2, 8]),
            MyVector(4, "r", 4, [1, 5, 12])
        ])

    def test_add_vector(self):
        vector = MyVector(5, "m", 1, [3, 3, 3])
        self.repo.add_vector(vector)
        self.assertIn(vector, self.repo.vectors)
        self.assertEqual(len(self.repo.vectors), 5)
        self.assertEqual(self.repo.get_at_index(4), vector)

    def test_get_at_index(self):
        vector = self.repo.get_at_index(0)
        self.assertEqual(vector.name_id, 1)
        self.assertEqual(vector.colour, "r")
        self.assertEqual(vector.values, [2, 2, 2])

    def test_update_vector(self):
        new_vector = MyVector(1, "y", 1, [10, 10, 10])
        self.repo.update_vector(0, new_vector)
        self.assertEqual(self.repo.get_at_index(0).colour, "y")
        self.assertEqual(self.repo.get_at_index(0).values, [10, 10, 10])
        self.assertEqual(self.repo.get_at_index(0).name_id, 1)

    def test_update_vector_by_id(self):
        new_vector = MyVector(2, "m", 2, [5, 5, 5])
        self.repo.update_vector_by_id(2, new_vector)
        self.assertEqual(self.repo.get_at_index(1).colour, "m")
        self.assertEqual(self.repo.get_at_index(1).values, [5, 5, 5])
        self.assertEqual(self.repo.get_at_index(1).name_id, 2)

    def test_delete_by_index(self):
        self.repo.delete_by_index(0)
        self.assertEqual(len(self.repo.vectors), 3)
        self.assertNotEqual(self.repo.get_at_index(0).name_id, 1)

    def test_delete_by_id(self):
        self.repo.delete_by_id(2)
        self.assertEqual(len(self.repo.vectors), 3)
        self.assertNotIn(2, [vector.name_id for vector in self.repo.vectors])

    def test_delete_all_vectors(self):
        self.repo.delete_all_vectors()
        self.assertEqual(len(self.repo.vectors), 0)

    def test_delete_by_color(self):
        self.repo.delete_by_color("r")
        self.assertEqual(len(self.repo.vectors), 2)
        self.assertNotIn("r", [vector.colour for vector in self.repo.vectors])

    def test_sum_by_color(self):
        total_sum = self.repo.sum_by_color("r")
        self.assertEqual(total_sum, 24)
        total_sum = self.repo.sum_by_color("b")
        self.assertEqual(total_sum, 5)
        total_sum = self.repo.sum_by_color("g")
        self.assertEqual(total_sum, 17)

    def test_add_scalar_to_all(self):
        self.repo.add_scalar_to_all(3)
        self.assertEqual(self.repo.get_at_index(0).values, [5, 5, 5])
        self.assertEqual(self.repo.get_at_index(1).values, [7, 3, 4])
        self.assertEqual(self.repo.get_at_index(2).values, [10, 5, 11])

if __name__ == '__main__':
    unittest.main()