from domain.Passenger import Passenger
from repository.PassengerRepository import PassengerRepository
from tests.PassengerValidator import PassengerValidator


class PassengerController:
    def __init__(self, repo: PassengerRepository):
        self.__repo = repo
        self.__validator = None

    def test_passenger(self, passenger: Passenger) -> bool:
        """
        Tests if a passenger is valid.
        :param passenger:
        :return:
        """
        try:
            self.__validator = PassengerValidator.validate(passenger)
        except ValueError as e:
            print(e)
            return False
        return True

    def add_passenger(self, first_name: str, last_name: str, passport_number: int) -> None:
        """
        Adds a passenger to the repository.
        :param first_name:
        :param last_name:
        :param passport_number:
        :return:
        """
        passenger = Passenger(first_name=first_name, last_name=last_name, passport_number=passport_number)
        if self.test_passenger(passenger):
            try:
                self.__repo.create(passenger)
            except ValueError as e:
                raise

    def remove_passenger(self, id: int) -> None:
        """
        Removes a passenger from the repository.
        :param id:
        :return:
        """
        try:
            passenger = self.__repo.find_by_id(id)

            if passenger is None:
                raise ValueError(f"Passenger with id {id} not found.")

            self.__repo.remove(passenger)

        except ValueError as e:
            raise

    def update_passenger(self, id: int, first_name: str | None = None,
                         last_name: str | None = None, passport_number: int | None = None) -> None:
        """
        Updates a passenger from the repository.
        :param id:
        :param first_name:
        :param last_name:
        :param passport_number:
        :return:
        """
        try:
            passenger = self.__repo.find_by_id(id)
            if passenger is None:
                raise ValueError(f"Passenger with id {id} not found.")

            if first_name is not None and len(first_name) > 0:
                passenger.first_name = first_name
            if last_name is not None and len(last_name) > 0:
                passenger.last_name = last_name
            if passport_number is not None and passport_number > 0:
                passenger.passport_number = passport_number

            if self.test_passenger(passenger):
                self.__repo.update(passenger)

        except ValueError as e:
            raise

    def get_all_passengers(self) -> list[Passenger]:
        """
        Returns all passengers from the repository.
        :return:
        """
        return self.__repo.get_all()






















