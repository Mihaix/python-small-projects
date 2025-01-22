from repository.PassengerRepository import PassengerRepository
from repository.PlaneRepository import PlaneRepository
from domain.Passenger import Passenger
from domain.Plane import Plane
from infrastructure.PassengerController import PassengerController
from infrastructure.PlaneController import PlaneController

class UI:
    def __init__(self) -> None:
        self.menu_options = [
            "1. Add passenger",
            "2. Get all passengers",
            "3. Update passenger by id",
            "4. Delete passenger by id",
            "5. Add plane",
            "6. Get all planes",
            "7. Update plane by number",
            "8. Delete plane by number",
            "9. Sort passengers by last name",
            "10. Sort planes by number of passengers",
            "11. Sorts the planes by the number of passengers whose first name starts with the given substring.",
            "12. Sorts the planes by the concatenation of the number of passengers and the destination.",
            "13. Identifies planes that have passengers with passport numbers starting with the same 3 digits.",
            "14. Identifies passengers from a given plane whose first name or last name contains the given substring.",
            "15. Identifies planes that have a passenger with the given name.",
            "16. Forms groups of k passengers from the same plane but with different last names.",
            "17. Forms groups of k planes with the same destination but belonging to different airline companies.",
            "q. Quit"
        ]
        self.passenger_repo = PassengerRepository()
        self.plane_repo = PlaneRepository()
        self.passenger_controller = PassengerController(self.passenger_repo)
        self.plane_controller = PlaneController(self.plane_repo)
        self.initialize_data()

    def initialize_data(self):
        passengers = [
            Passenger(first_name="John", last_name="Doe", passport_number=123456),
            Passenger(first_name="Jane", last_name="Smith", passport_number=123321),
            Passenger(first_name="Alice", last_name="Johnson", passport_number=111222),
            Passenger(first_name="Bob", last_name="Brown", passport_number=333444),
            Passenger(first_name="Charlie", last_name="Davis", passport_number=555666)
        ]
        for passenger in passengers:
            self.passenger_repo.create(passenger)

        planes = [
            Plane(number=1, airline_company="Airline A", number_of_seats=150, destination="New York", list_of_passengers=passengers[:3]),
            Plane(number=2, airline_company="Airline B", number_of_seats=200, destination="Los Angeles", list_of_passengers=passengers[1:3]),
            Plane(number=3, airline_company="Airline C", number_of_seats=180, destination="Chicago", list_of_passengers=passengers[2:4]),
            Plane(number=4, airline_company="Airline D", number_of_seats=220, destination="Miami", list_of_passengers=passengers[3:]),
            Plane(number=5, airline_company="Airline E", number_of_seats=160, destination="San Francisco", list_of_passengers=passengers[:3])
        ]
        for plane in planes:
            self.plane_repo.create(plane)

    def print_menu(self):
        for op in self.menu_options:
            print(op)

    def read_passenger_info(self):
        while True:
            try:
                first_name = input("First name: ")
                last_name = input("Last name: ")
                passport_number = int(input("Passport number: "))
                return first_name, last_name, passport_number
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def read_plane_info(self):
        while True:
            try:
                number = int(input("Plane number: "))
                airline_company = input("Airline company: ")
                number_of_seats = int(input("Number of seats: "))
                destination = input("Destination: ")
                passengers = []
                while True:
                    add_passenger = input("Add a passenger? (y/n): ").lower()
                    if add_passenger == 'y':
                        passenger_info = self.read_passenger_info()
                        passenger = Passenger(*passenger_info)
                        passengers.append(passenger)
                    elif add_passenger == 'n':
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                return number, airline_company, number_of_seats, destination, passengers
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def read_update_plane_info(self):
        while True:
            try:
                airline_company = input("Airline company: ")
                number_of_seats = int(input("Number of seats: "))
                destination = input("Destination: ")
                passengers = []
                while True:
                    add_passenger = input("Add a passenger? (y/n): ").lower()
                    if add_passenger == 'y':
                        passenger_info = self.read_passenger_info()
                        passenger = Passenger(*passenger_info)
                        passengers.append(passenger)
                    elif add_passenger == 'n':
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                return airline_company, number_of_seats, destination, passengers
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def run(self):
        while True:
            self.print_menu()
            option = input("Option: ")
            try:
                match option:
                    case "1":
                        passenger_info = self.read_passenger_info()
                        self.passenger_controller.add_passenger(*passenger_info)
                    case "2":
                        print(self.passenger_controller.get_all_passengers())
                    case "3":
                        passenger_id = int(input("Passenger ID: "))
                        passenger_info = self.read_passenger_info()
                        self.passenger_controller.update_passenger(passenger_id, *passenger_info)
                    case "4":
                        passenger_id = int(input("Passenger ID: "))
                        self.passenger_controller.remove_passenger(passenger_id)
                    case "5":
                        plane_info = self.read_plane_info()
                        self.plane_controller.add_plane(*plane_info)
                    case "6":
                        print(self.plane_controller.get_planes())
                    case "7":
                        plane_number = int(input("Plane number: "))
                        plane_info = self.read_update_plane_info()
                        self.plane_controller.update_plane(plane_number, *plane_info)
                    case "8":
                        plane_number = int(input("Plane number: "))
                        self.plane_controller.remove_plane(plane_number)
                    case "9":
                        plane_number = int(input("Plane number: "))
                        plane = self.plane_controller.get_planes()[plane_number - 1]
                        self.plane_controller.sort_passengers_by_last_name(plane)
                    case "10":
                        self.plane_controller.sort_planes_by_number_of_passengers()
                    case "11":
                        substring = input("Substring: ")
                        self.plane_controller.sort_planes_by_passenger_first_name_substring(substring)
                    case "12":
                        self.plane_controller.sort_planes_by_passenger_count_and_destination()
                    case "13":
                        print(self.plane_controller.identify_passengers_with_similar_passport_numbers())
                    case "14":
                        plane_number = int(input("Plane number: "))
                        substring = input("Substring: ")
                        plane = self.plane_controller.get_planes()[plane_number - 1]
                        print(self.plane_controller.identify_passengers_by_name_substring(plane, substring))
                    case "15":
                        name = input("Name: ")
                        print(self.plane_controller.identify_planes_with_passenger_name(name))
                    case "16":
                        plane_number = int(input("Plane number: "))
                        k = int(input("Group size: "))
                        plane = self.plane_controller.get_planes()[plane_number - 1]
                        print(self.plane_controller.form_groups_of_passengers_with_different_last_name(plane, k))
                    case "17":
                        k = int(input("Group size: "))
                        print(self.plane_controller.form_groups_of_planes_with_different_airline_companies(self.plane_controller.get_planes(), k))
                    case "q":
                        break
                    case _:
                        print("Invalid option")
            except Exception as e:
                print(f"An error occurred: {e}")
