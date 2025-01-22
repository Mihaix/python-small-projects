from domain import Passenger

class PassengerRepository:
    def __init__(self):
        self.__objects: list[Passenger] = []

    @property
    def objects(self) -> list[Passenger]:
        return self.__objects

    @objects.setter
    def objects(self, objects: list[Passenger]) -> None:
        self.__objects = objects

    def create(self, obj: Passenger) -> None:
        """
        Add a new object to the repository
        :param obj:
        :return:
        """
        self.__objects.append(obj)

    def get_all(self) -> list[Passenger]:
        """
        Get all objects from the repository
        :return:
        """
        return self.objects

    def remove(self, obj: Passenger) -> None:
        """
        Remove an object from the repository
        :param obj:
        :return:
        """
        if self.find(obj) is None:
            raise ValueError(f"Object {obj} not found.")
        self.__objects.remove(obj)

    def find(self, obj: Passenger) -> int | None:
        """
        Find an object in the repository
        :param obj:
        :return:
        """
        try:
            return self.objects.index(obj)
        except ValueError:
            return None

    def find_by_id(self, id: int):
        """
        Find an object by its id
        :param id:
        :return: Passenger | None
        """
        objects =  [obj for obj in self.objects if obj.id == id]
        if len(objects) != 0:
            return objects[0]
        return None

    def update(self, obj: Passenger) -> None:
        """
        Update an object in the repository
        :param obj:
        :return:
        """
        index = self.find(obj)
        if index is None:
            raise ValueError(f"Object {obj} does not exist.")
        else:
            self.__objects[index] = obj