from domain.Passenger import Passenger
from domain.Plane import Plane
from repository.PlaneRepository import PlaneRepository
from tests.PlaneValidator import PlaneValidator
from utils.utils import sort, filter, backtracking

class PlaneController:
    def __init__(self, repo: PlaneRepository):
        self.__repo = repo
        self.__validator = None

    def test_plane(self, plane: Plane) -> bool:
        """
        Tests if a plane is valid.
        :param plane:
        :return:
        """
        try:
            self.__validator = PlaneValidator.validate(plane)
        except ValueError as e:
            print(e)
            return False
        return True

    def add_plane(self, number: int, airline_company: str, number_of_seats: int,
                  destination: str, passengers: list[Passenger]) -> None:
        """
        Adds a plane to the repository.
        :param number:
        :param airline_company:
        :param number_of_seats:
        :param destination:
        :param passengers:
        :return:
        """
        plane = Plane(number, airline_company, number_of_seats, destination, passengers)
        if self.test_plane(plane):
            try:
                self.__repo.create(plane)
            except ValueError as e:
                raise

    def remove_plane(self, number: int) -> None:
        """
        Removes a plane from the repository.
        :param number:
        :return:
        """
        try:
            plane = self.__repo.find_by_id(number)

            if plane is None:
                raise ValueError(f"Plane with number {number} not found.")

            self.__repo.remove(plane)

        except ValueError as e:
            raise

    def update_plane(self, number: int, airline_company: str | None = None, number_of_seats: int | None = None,
                     destination: str | None = None, passengers: list[Passenger] | None = None) -> None:
        """
        Updates a plane from the repository.
        :param number:
        :param airline_company:
        :param number_of_seats:
        :param destination:
        :param passengers:
        :return:
        """
        try:
            plane = self.__repo.find_by_id(number)
            if plane is None:
                raise ValueError(f"Plane with number {number} not found.")

            if airline_company is not None and len(airline_company) > 0:
                plane.airline_company = airline_company
            if number_of_seats is not None and number_of_seats > 0:
                plane.number_of_seats = number_of_seats
            if destination is not None and len(destination) > 0:
                plane.destination = destination
            if passengers is not None and not passengers == []:
                plane.list_of_passengers = passengers

            if self.test_plane(plane):
                self.__repo.update(plane)

        except ValueError as e:
            raise

    def get_planes(self) -> list[Plane]:
        """
        Gets all the planes from the repository.
        :return:
        """
        return self.__repo.get_all()

    def sort_passengers_by_last_name(self, plane: Plane) -> None:
        """
        Sorts the passengers of a plane by last name.
        :param plane:
        :return:
        """
        plane.list_of_passengers = sort(plane.list_of_passengers, key_func=lambda passenger: passenger.last_name)

    def sort_planes_by_number_of_passengers(self) -> None:
        """
        Sorts the planes by the number of passengers.
        :return:
        """
        self.__repo.objects = sort(self.__repo.objects, key_func=lambda plane: len(plane.list_of_passengers))

    def sort_planes_by_passenger_first_name_substring(self, substring: str) -> None:
        """
        Sorts the planes by the number of passengers whose first name starts with the given substring.
        :param substring:
        :return:
        """
        self.__repo.objects = sort(
            self.__repo.objects,
            key_func=lambda plane: sum(
                1 for passenger in plane.list_of_passengers if passenger.first_name.startswith(substring))
        )

    def sort_planes_by_passenger_count_and_destination(self) -> None:
        """
        Sorts the planes by the concatenation of the number of passengers and the destination.
        :return:
        """
        self.__repo.objects = sort(
            self.__repo.objects,
            key_func=lambda plane: f"{len(plane.list_of_passengers)}{plane.destination}"
        )

    def identify_passengers_with_similar_passport_numbers(self) -> list[Plane]:
        """
        Identifies planes that have passengers with passport numbers starting with the same 3 digits.
        :return:
        """
        return filter(
            self.__repo.get_all(),
            lambda plane: len(set(str(passport.passport_number)[:3] for passport in plane.list_of_passengers)) != len(
                plane.list_of_passengers),
            True
        )

    def identify_passengers_by_name_substring(self, plane: Plane, substring: str) -> list[Passenger]:
        """
        Identifies passengers from a given plane whose first name or last name contains the given substring.
        :param plane:
        :param substring:
        :return:
        """
        return filter(
            plane.list_of_passengers,
            lambda passenger: substring.lower() in passenger.first_name.lower() or substring.lower() in passenger.last_name.lower(),
            True
        )

    def identify_planes_with_passenger_name(self, name: str) -> list[Plane]:
        """
        Identifies planes that have a passenger with the given name.
        :param name:
        :return:
        """
        return filter(
            self.__repo.get_all(),
            lambda plane: any(
                name.lower() == passenger.first_name.lower() or name.lower() == passenger.last_name.lower() for
                passenger in plane.list_of_passengers),
            True
        )

    def form_groups_of_passengers_with_different_last_name(self, plane: Plane, k: int) -> list[list[Passenger]]:
        """
        Forms groups of k passengers from the same plane but with different last names.
        :param plane:
        :param k:
        :return:
        """
        return backtracking(
            plane.list_of_passengers,
            lambda group: len(set(p.last_name for p in group)) == k,
            k
        )

    def form_groups_of_planes_with_different_airline_companies(self, planes: list[Plane], k: int) -> list[list[Plane]]:
        """
        Forms groups of k planes with the same destination but belonging to different airline companies.
        :param planes:
        :param k:
        :return:
        """
        backtracking(
            planes,
            lambda group: len(set(p.airline_company for p in group)) == k and len(
                set(p.destination for p in group)) == 1,
            k
        )
