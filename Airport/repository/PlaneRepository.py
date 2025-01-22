from domain import Plane

class PlaneRepository:
    def __init__(self):
        self.__objects: list[Plane] = []

    @property
    def objects(self) -> list[Plane]:
        return self.__objects

    @objects.setter
    def objects(self, objects: list[Plane]) -> None:
        self.__objects = objects

    def create(self, obj: Plane) -> None:
        """
        Add an object to the repository.
        :param obj:
        :return:
        """
        self.__objects.append(obj)

    def get_all(self) -> list[Plane]:
        """
        Get all objects from the repository.
        :return:
        """
        return self.objects

    def remove(self, obj: Plane) -> None:
        """
        Remove an object from the repository.
        :param obj:
        :return:
        """
        if self.find(obj) is None:
            raise ValueError(f"Object {obj} not found.")
        self.__objects.remove(obj)

    def find(self, obj: Plane) -> int | None:
        """
        Find an object in the repository.
        :param obj:
        :return:
        """
        try:
            return self.objects.index(obj)
        except ValueError:
            return None

    def find_by_id(self, id: int):
        """
        Find an object by its id.
        :param id:
        :return: Plane | None
        """
        objects =  [obj for obj in self.objects if obj.number == id]
        if len(objects) != 0:
            return objects[0]
        return None

    def update(self, obj: Plane) -> None:
        """
        Update an object in the repository.
        :param obj:
        :return:
        """
        index = self.find(obj)
        if index is None:
            raise ValueError(f"Object {obj} does not exists.")
        else:
            self.__objects[index] = obj
