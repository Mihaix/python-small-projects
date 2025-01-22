import unittest
from domain.Passenger import Passenger
from repository.PassengerRepository import PassengerRepository
from infrastructure.PassengerController import PassengerController

class TestPassengerController(unittest.TestCase):

    def setUp(self):
        self.repo = PassengerRepository()
        self.controller = PassengerController(self.repo)

    def test_add_passenger(self):
        self.controller.add_passenger("John", "Doe", 123456)
        passengers = self.controller.get_all_passengers()
        self.assertEqual(len(passengers), 1)
        self.assertEqual(passengers[0].first_name, "John")
        self.assertEqual(passengers[0].passport_number, 123456)

    def test_remove_passenger(self):
        self.controller.add_passenger("John", "Doe", 123456)
        passenger = self.controller.get_all_passengers()[0]
        self.controller.remove_passenger(passenger.id)
        passengers = self.controller.get_all_passengers()
        self.assertEqual(len(passengers), 0)
        self.assertRaises(ValueError, self.controller.remove_passenger, passenger.id)

    def test_update_passenger(self):
        self.controller.add_passenger("John", "Doe", 123456)
        passenger = self.controller.get_all_passengers()[0]
        self.controller.update_passenger(passenger.id, first_name="Jane")
        updated_passenger = self.controller.get_all_passengers()[0]
        self.assertEqual(updated_passenger.first_name, "Jane")
        self.assertEqual(updated_passenger.last_name, "Doe")
        self.assertEqual(updated_passenger.passport_number, 123456)

    def test_get_all_passengers(self):
        self.controller.add_passenger("John", "Doe", 123456)
        self.controller.add_passenger("Jane", "Smith", 654321)
        passengers = self.controller.get_all_passengers()
        self.assertEqual(len(passengers), 2)
        self.assertEqual(passengers[0].first_name, "John")
        self.assertEqual(passengers[1].first_name, "Jane")

if __name__ == '__main__':
    unittest.main()