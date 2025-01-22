import numpy as np

class MyVector:

    VALID_COLORS = ["r", "g", "b", "y", "m"]

    def __init__(self, name_id: str | int = 0, colour: str = "", type: int = 1, values: list[int] = None):
        self.__name_id = name_id

        if colour not in self.VALID_COLORS:
            raise ValueError(f"Color must be one of the following: {', '.join(self.VALID_COLORS)}")
        self.__colour = colour

        if type < 1:
            raise ValueError("Type must be a positive integer")
        self.__type = type

        self.__values = np.array(values if values is not None else [])

    @property
    def name_id(self) -> str | int:
        return self.__name_id

    @name_id.setter
    def name_id(self, name_id: str | int) -> None:
        self.__name_id = name_id

    @property
    def colour(self) -> str:
        return self.__colour

    @colour.setter
    def colour(self, colour: str) -> None:
        if colour not in self.VALID_COLORS:
            raise ValueError(f"Color must be one of the following: {', '.join(self.VALID_COLORS)}")
        self.__colour = colour

    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int) -> None:
        if type < 1:
            raise ValueError("Type must be a positive integer")
        self.__type = type

    @property
    def values(self) -> list[int]:
        return self.__values.tolist()

    @values.setter
    def values(self, values: list[int]) -> None:
        self.__values = np.array(values if values is not None else [])

    def add_scalar(self, scalar: int) -> None:
        self.__values += scalar

    def add(self, vector: list[int]) -> None:
        if len(self.__values) != len(vector):
            raise ValueError("Both vectors must have the same length")
        self.__values += np.array(vector)

    def subtract(self, vector: list[int]) -> None:
        if len(self.__values) != len(vector):
            raise ValueError("Both vectors must have the same length")
        self.__values -= np.array(vector)

    def multiplication(self, vector: list[int]) -> int:
        if len(self.__values) != len(vector):
            raise ValueError("Both vectors must have the same length")
        return int(np.dot(self.__values, np.array(vector)))

    def sum(self) -> int:
        return int(np.sum(self.__values))

    def product(self) -> int:
        return int(np.prod(self.__values))

    def average(self) -> float:
        return float(np.mean(self.__values))

    def minimum(self) -> int:
        return int(np.min(self.__values))

    def maximum(self) -> int:
        return int(np.max(self.__values))

    def __str__(self) -> str:
        return f"Vector {self.__name_id} with colour {self.__colour}, type {self.__type} and values {self.__values.tolist()}"

    def __repr__(self) -> str:
        return f"MyVector({self.__name_id}, {self.__colour}, {self.__type}, {self.__values.tolist()})"
