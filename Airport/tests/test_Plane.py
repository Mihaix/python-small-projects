import unittest
from domain.Plane import Plane
from domain.Passenger import Passenger

class TestPlane(unittest.TestCase):

    def test_plane_initialization(self):
        plane = Plane(number=1, airline_company="Airline", number_of_seats=100, destination="Destination")
        self.assertEqual(plane.number, 1)
        self.assertEqual(plane.airline_company, "Airline")
        self.assertEqual(plane.number_of_seats, 100)
        self.assertEqual(plane.destination, "Destination")
        self.assertEqual(plane.list_of_passengers, [])

    def test_plane_setters(self):
        plane = Plane()
        plane.number = 2
        plane.airline_company = "New Airline"
        plane.number_of_seats = 200
        plane.destination = "New Destination"
        self.assertEqual(plane.number, 2)
        self.assertEqual(plane.airline_company, "New Airline")
        self.assertEqual(plane.number_of_seats, 200)
        self.assertEqual(plane.destination, "New Destination")

    def test_plane_passengers(self):
        passenger1 = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(first_name="Jane", last_name="Doe", passport_number=654321)
        plane = Plane(list_of_passengers=[passenger1, passenger2])
        self.assertEqual(len(plane.list_of_passengers), 2)
        self.assertEqual(plane.list_of_passengers[0].first_name, "John")
        self.assertEqual(plane.list_of_passengers[1].first_name, "Jane")

    def test_plane_equality(self):
        plane1 = Plane(number=1)
        plane2 = Plane(number=1)
        plane3 = Plane(number=2)
        self.assertTrue(plane1 == plane2)
        self.assertFalse(plane1 == plane3)
        self.assertFalse(plane1 == "not a plane")

if __name__ == '__main__':
    unittest.main()