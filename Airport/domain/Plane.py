from domain import Passenger

class Plane:
    def __init__(self, number: int = 0, airline_company: str = "", number_of_seats: int = 0,
                 destination: str = "", list_of_passengers: list[Passenger] = None):
        self.__number = number
        self.__airline_company = airline_company
        self.__number_of_seats = number_of_seats
        self.__destination = destination
        self.__list_of_passengers = list_of_passengers if list_of_passengers is not None else []

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def airline_company(self):
        return self.__airline_company

    @airline_company.setter
    def airline_company(self, airline_company):
        self.__airline_company = airline_company

    @property
    def number_of_seats(self):

        return self.__number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, number_of_seats):
        self.__number_of_seats = number_of_seats

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination):
        self.__destination = destination

    @property
    def list_of_passengers(self):
        return self.__list_of_passengers

    @list_of_passengers.setter
    def list_of_passengers(self, list_of_passengers):
        self.__list_of_passengers = list_of_passengers

    def __str__(self):
        return f"Plane(number={self.__number}, airline_company={self.__airline_company}, " \
               f"number_of_seats={self.__number_of_seats}, destination={self.__destination}, " \
               f"list_of_passengers={self.__list_of_passengers})\n"

    def __repr__(self):
        return f"Plane(number={self.__number}, airline_company={self.__airline_company}, " \
               f"number_of_seats={self.__number_of_seats}, destination={self.__destination}, " \
               f"list_of_passengers={self.__list_of_passengers})\n"

    def __eq__(self, p):
        if isinstance(p, Plane):
            return self.__number == p.__number
        return False

