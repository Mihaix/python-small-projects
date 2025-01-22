import unittest
from domain.Passenger import Passenger
from domain.Plane import Plane
from repository.PlaneRepository import PlaneRepository
from infrastructure.PlaneController import PlaneController

class TestPlaneController(unittest.TestCase):

    def setUp(self):
        self.repo = PlaneRepository()
        self.controller = PlaneController(self.repo)

    def test_add_plane(self):
        self.controller.add_plane(1, "Airline A", 150, "City A", [])
        planes = self.controller.get_planes()
        self.assertEqual(len(planes), 1)
        self.assertEqual(planes[0].airline_company, "Airline A")
        self.assertEqual(planes[0].number_of_seats, 150)

    def test_remove_plane(self):
        self.controller.add_plane(1, "Airline A", 150, "City A", [])
        self.controller.add_plane(2, "Airline B", 10, "City X", [])
        self.controller.remove_plane(1)
        planes = self.controller.get_planes()
        self.assertEqual(len(planes), 1)
        self.assertRaises(ValueError, self.controller.remove_plane, 1)
        self.assertIsNotNone(self.controller.get_planes())

    def test_update_plane(self):
        self.controller.add_plane(1, "Airline A", 150, "City A", [])
        self.controller.update_plane(1, airline_company="Airline B")
        plane = self.controller.get_planes()[0]
        self.assertEqual(plane.airline_company, "Airline B")
        self.assertEqual(plane.number_of_seats, 150)
        self.assertEqual(plane.destination, "City A")

    def test_sort_planes_by_number_of_passengers(self):
        passenger1 = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(first_name="Jane", last_name="Smith", passport_number=654321)
        self.controller.add_plane(1, "Airline A", 150, "City A", [passenger1])
        self.controller.add_plane(2, "Airline B", 200, "City B", [passenger1, passenger2])
        self.controller.sort_planes_by_number_of_passengers()
        planes = self.controller.get_planes()
        self.assertEqual(planes[0].number, 1)
        self.assertEqual(planes[1].number, 2)
        self.assertEqual(len(planes[0].list_of_passengers), 1)

    def test_identify_passengers_with_similar_passport_numbers(self):
        passenger1 = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(first_name="Jane", last_name="Smith", passport_number=123789)
        self.controller.add_plane(1, "Airline A", 150, "City A", [passenger1, passenger2])
        planes = self.controller.identify_passengers_with_similar_passport_numbers()
        self.assertEqual(len(planes), 1)
        self.assertEqual(planes[0].number, 1)
        self.assertEqual(len(planes[0].list_of_passengers), 2)

    def test_identify_planes_with_passenger_name(self):
        passenger1 = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(first_name="Jane", last_name="Smith", passport_number=654321)
        self.controller.add_plane(1, "Airline A", 150, "City A", [passenger1])
        self.controller.add_plane(2, "Airline B", 200, "City B", [passenger2])
        planes = self.controller.identify_planes_with_passenger_name("John")
        self.assertEqual(len(planes), 1)
        self.assertEqual(planes[0].number, 1)
        self.assertEqual(planes[0].list_of_passengers[0].first_name, "John")

    def test_sort_passengers_by_last_name(self):
        passenger1 = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(first_name="Jane", last_name="Smith", passport_number=654321)
        plane = Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="City A", list_of_passengers=[passenger2, passenger1])
        self.controller.add_plane(1, "Airline A", 150, "City A", [passenger2, passenger1])
        self.controller.sort_passengers_by_last_name(plane)
        self.assertEqual(plane.list_of_passengers[0].last_name, "Doe")
        self.assertEqual(plane.list_of_passengers[1].last_name, "Smith")
        self.assertEqual(len(plane.list_of_passengers), 2)

    def test_sort_planes_by_passenger_first_name_substring(self):
        passenger1 = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(first_name="Jane", last_name="Smith", passport_number=654321)
        self.controller.add_plane(1, "Airline A", 150, "City A", [passenger1])
        self.controller.add_plane(2, "Airline B", 200, "City B", [passenger2])
        self.controller.sort_planes_by_passenger_first_name_substring("Ja")
        planes = self.controller.get_planes()
        self.assertEqual(planes[0].number, 2)
        self.assertEqual(planes[1].number, 1)
        self.assertEqual(len(planes[0].list_of_passengers), 1)

    def test_sort_planes_by_passenger_count_and_destination(self):
        passenger1 = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(first_name="Jane", last_name="Smith", passport_number=654321)
        self.controller.add_plane(1, "Airline A", 150, "City A", [passenger1])
        self.controller.add_plane(2, "Airline B", 200, "City A", [passenger1, passenger2])
        self.controller.sort_planes_by_passenger_count_and_destination()
        planes = self.controller.get_planes()
        self.assertEqual(planes[0].number, 1)
        self.assertEqual(planes[1].number, 2)
        self.assertEqual(planes[0].destination, "City A")

    def test_identify_passengers_by_name_substring(self):
        passenger1 = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(first_name="Jane", last_name="Smith", passport_number=654321)
        plane = Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="City A", list_of_passengers=[passenger1, passenger2])
        self.controller.add_plane(1, "Airline A", 150, "City A", [passenger1, passenger2])
        passengers = self.controller.identify_passengers_by_name_substring(plane, "Jo")
        self.assertEqual(len(passengers), 1)
        self.assertEqual(passengers[0].first_name, "John")
        self.assertEqual(passengers[0].last_name, "Doe")

    def test_form_groups_of_passengers_with_different_last_name(self):
        passenger1 = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(first_name="Jane", last_name="Smith", passport_number=654321)
        passenger3 = Passenger(first_name="Jim", last_name="Brown", passport_number=789123)
        plane = Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="City A", list_of_passengers=[passenger1, passenger2, passenger3])
        self.controller.add_plane(1, "Airline A", 150, "City A", [passenger1, passenger2, passenger3])
        groups = self.controller.form_groups_of_passengers_with_different_last_name(plane, 2)
        self.assertEqual(len(groups), 3)
        self.assertEqual(len(groups[0]), 2)
        self.assertEqual(len(groups[1]), 2)

    def test_form_groups_of_planes_with_different_airline_companies(self):
        plane1 = Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="City A")
        plane2 = Plane(number=2, airline_company="Airline B", number_of_seats=200, destination="City A")
        plane3 = Plane(number=3, airline_company="Airline C", number_of_seats=250, destination="City A")
        self.controller.add_plane(1, "Airline A", 150, "City A", [])
        self.controller.add_plane(2, "Airline B", 200, "City A", [])
        self.controller.add_plane(3, "Airline C", 250, "City A", [])
        groups = self.controller.form_groups_of_planes_with_different_airline_companies(self.controller.get_planes(), 2)
        self.assertEqual(len(groups), 3)
        self.assertEqual(len(groups[0]), 2)
        self.assertEqual(groups[0][0].destination, "City A")

if __name__ == '__main__':
    unittest.main()