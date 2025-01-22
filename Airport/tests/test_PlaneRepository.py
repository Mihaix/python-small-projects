import unittest
from domain.Plane import Plane
from repository.PlaneRepository import PlaneRepository

class TestPlaneRepository(unittest.TestCase):

    def setUp(self):
        self.repo = PlaneRepository()

    def test_create(self):
        plane = Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="City A")
        self.repo.create(plane)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.get_all()[0].airline_company, "Airline A")
        self.assertEqual(self.repo.get_all()[0].number_of_seats, 150)

    def test_get_all(self):
        plane1 = Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="City A")
        plane2 = Plane(number=2, airline_company="Airline B", number_of_seats=200, destination="City B")
        self.repo.create(plane1)
        self.repo.create(plane2)
        all_planes = self.repo.get_all()
        self.assertEqual(len(all_planes), 2)
        self.assertEqual(all_planes[0].airline_company, "Airline A")
        self.assertEqual(all_planes[1].airline_company, "Airline B")

    def test_remove(self):
        plane = Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="City A")
        self.repo.create(plane)
        self.repo.remove(plane)
        self.assertEqual(len(self.repo.get_all()), 0)
        self.assertIsNone(self.repo.find(plane))
        self.assertRaises(ValueError, self.repo.remove, plane)

    def test_find(self):
        plane = Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="City A")
        self.repo.create(plane)
        index = self.repo.find(plane)
        self.assertIsNotNone(index)
        self.assertEqual(index, 0)
        self.assertEqual(self.repo.get_all()[index].airline_company, "Airline A")

    def test_find_by_id(self):
        plane = Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="City A")
        self.repo.create(plane)
        found_plane = self.repo.find_by_id(plane.number)
        self.assertIsNotNone(found_plane)
        self.assertEqual(found_plane.number, plane.number)
        self.assertEqual(found_plane.airline_company, "Airline A")

    def test_update(self):
        plane = Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="City A")
        self.repo.create(plane)
        plane.airline_company = "Airline B"
        self.repo.update(plane)
        updated_plane = self.repo.find_by_id(plane.number)
        self.assertEqual(updated_plane.airline_company, "Airline B")
        self.assertEqual(updated_plane.number_of_seats, 150)
        self.assertEqual(updated_plane.destination, "City A")

if __name__ == '__main__':
    unittest.main()