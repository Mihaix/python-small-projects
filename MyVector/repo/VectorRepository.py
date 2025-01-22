from domain.MyVector import MyVector
import matplotlib.pyplot as plt

class VectorRepository:

    def __init__(self, vectors: list[MyVector] = None):
        self.__vectors = vectors if vectors is not None else []

    @property
    def vectors(self) -> list[MyVector]:
        return self.__vectors

    def add_vector(self, vector: MyVector) -> None:
        """
        Adds a vector to the repository.
        :param vector:
        :return:
        """
        self.__vectors.append(vector)

    def get_at_index(self, index: int) -> MyVector:
        """
        Returns the vector at the given index.
        :param index:
        :return:
        """
        return self.__vectors[index]

    def update_vector(self, index: int, vector: MyVector) -> None:
        """
        Updates the vector at the given index.
        :param index:
        :param vector:
        :return:
        """
        self.__vectors[index] = vector

    def update_vector_by_id(self, name_id: str | int, vector: MyVector) -> None:
        """
        Updates the vector with the given id.
        :param name_id:
        :param vector:
        :return:
        """
        for i in range(len(self.__vectors)):
            if self.__vectors[i].name_id == name_id:
                self.__vectors[i] = vector
                return

    def delete_by_index(self, index: int) -> None:
        """
        Deletes the vector at the given index.
        :param index:
        :return:
        """
        del self.__vectors[index]

    def delete_by_id(self, name_id: str | int) -> None:
        """
        Deletes the vector with the given id.
        :param name_id:
        :return:
        """
        for i in range(len(self.__vectors)):
            if self.__vectors[i].name_id == name_id:
                del self.__vectors[i]
                return

    def plot_vectors(self) -> None:
        """
        Plots the vectors based on their type and colour.
        :return:
        """
        marker_map = {1: 'o', 2: 's', 3: '^'}
        for vector in self.__vectors:
            marker = marker_map.get(vector.type, 'D')
            plt.plot(vector.values, color=vector.colour, marker=marker)
        plt.show()

    def sum_by_color(self, color: str) -> int:
        """
        Returns the sum of the values of the vectors with the given colour.
        :param color:
        :return:
        """
        total_sum = 0
        for vector in self.__vectors:
            if vector.colour == color:
                total_sum += vector.sum()
        return total_sum

    def delete_all_vectors(self) -> None:
        """
        Deletes all vectors from the repository.
        :return:
        """
        self.__vectors.clear()

    def delete_by_color(self, color: str) -> None:
        """
        Deletes all vectors with the given colour.
        :param color:
        :return:
        """
        self.__vectors = [vector for vector in self.__vectors if vector.colour != color]

    def add_scalar_to_all(self, scalar: int) -> None:
        """
        Adds a scalar to all vectors.
        :param scalar:
        :return:
        """
        for vector in self.__vectors:
            vector.add_scalar(scalar)

    def __str__(self):
        return f"VectorRepository vectors: {self.__vectors}"