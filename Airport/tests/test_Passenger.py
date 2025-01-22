import unittest
from domain.Passenger import Passenger

class TestPassenger(unittest.TestCase):

    def test_passenger_initialization(self):
        passenger = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        self.assertEqual(passenger.first_name, "John")
        self.assertEqual(passenger.last_name, "Doe")
        self.assertEqual(passenger.passport_number, 123456)
        self.assertIsNotNone(passenger.id)

    def test_passenger_setters(self):
        passenger = Passenger()
        passenger.first_name = "Jane"
        passenger.last_name = "Smith"
        passenger.passport_number = 654321
        self.assertEqual(passenger.first_name, "Jane")
        self.assertEqual(passenger.last_name, "Smith")
        self.assertEqual(passenger.passport_number, 654321)

    def test_passenger_equality(self):
        passenger1 = Passenger(id=1, first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(id=1, first_name="Jane", last_name="Smith", passport_number=654321)
        passenger3 = Passenger(id=2, first_name="John", last_name="Doe", passport_number=123456)
        self.assertTrue(passenger1 == passenger2)
        self.assertFalse(passenger1 == passenger3)
        self.assertFalse(passenger1 == "not a passenger")

if __name__ == '__main__':
    unittest.main()