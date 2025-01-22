import unittest
from domain.Passenger import Passenger
from repository.PassengerRepository import PassengerRepository

class TestPassengerRepository(unittest.TestCase):

    def setUp(self):
        self.repo = PassengerRepository()

    def test_create(self):
        passenger = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        self.repo.create(passenger)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.get_all()[0].first_name, "John")
        self.assertEqual(self.repo.get_all()[0].passport_number, 123456)

    def test_get_all(self):
        passenger1 = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        passenger2 = Passenger(first_name="Jane", last_name="Smith", passport_number=654321)
        self.repo.create(passenger1)
        self.repo.create(passenger2)
        all_passengers = self.repo.get_all()
        self.assertEqual(len(all_passengers), 2)
        self.assertEqual(all_passengers[0].first_name, "John")
        self.assertEqual(all_passengers[1].first_name, "Jane")

    def test_remove(self):
        passenger = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        self.repo.create(passenger)
        self.repo.remove(passenger)
        self.assertEqual(len(self.repo.get_all()), 0)
        self.assertIsNone(self.repo.find(passenger))
        self.assertRaises(ValueError, self.repo.remove, passenger)

    def test_find(self):
        passenger = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        self.repo.create(passenger)
        index = self.repo.find(passenger)
        self.assertIsNotNone(index)
        self.assertEqual(index, 0)
        self.assertEqual(self.repo.get_all()[index].first_name, "John")

    def test_find_by_id(self):
        passenger = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        self.repo.create(passenger)
        found_passenger = self.repo.find_by_id(passenger.id)
        self.assertIsNotNone(found_passenger)
        self.assertEqual(found_passenger.id, passenger.id)
        self.assertEqual(found_passenger.first_name, "John")

    def test_update(self):
        passenger = Passenger(first_name="John", last_name="Doe", passport_number=123456)
        self.repo.create(passenger)
        passenger.first_name = "Jane"
        self.repo.update(passenger)
        updated_passenger = self.repo.find_by_id(passenger.id)
        self.assertEqual(updated_passenger.first_name, "Jane")
        self.assertEqual(updated_passenger.last_name, "Doe")
        self.assertEqual(updated_passenger.passport_number, 123456)

if __name__ == '__main__':
    unittest.main()