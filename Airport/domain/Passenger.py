class Passenger:
    _id_counter = 1

    def __init__(self, id: int = None, first_name: str = "", last_name: str = "", passport_number: int = 0):
        if id is None:
            self.__id = Passenger._id_counter
            Passenger._id_counter += 1
        else:
            self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__passport_number = passport_number

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def passport_number(self):
        return self.__passport_number

    @passport_number.setter
    def passport_number(self, passport_number):
        self.__passport_number = passport_number

    def __str__(self):
        return f"Passenger {self.__id} {self.__first_name} {self.__last_name} with passport {self.__passport_number}."

    def __repr__(self):
        return f"Passenger {self.__id} {self.__first_name} {self.__last_name} with passport: {self.__passport_number}"

    def __eq__(self, p):
        if isinstance(p, Passenger):
            return self.__id == p.__id
        return False
