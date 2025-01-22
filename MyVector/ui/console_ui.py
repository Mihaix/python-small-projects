from repo.VectorRepository import VectorRepository
from domain.MyVector import MyVector

class UI:
    def __init__(self) -> None:
        self.menu_options = ["1. Add vector",
                             "2. Get all vectors",
                             "3. Get vector by index",
                             "4. Get vector by id",
                             "5. Update vector by index",
                             "6. Update vector by id",
                             "7. Delete vector by index",
                             "8. Delete vector by id",
                             "9. Plot vectors",
                             "10. Sum values of vectors by color",
                             "11. Add scalar to all vectors",
                             "12. Add scalar to a vector",
                             "13. Add two vectors",
                             "14. Subtract two vectors",
                             "15. Multiply two vectors",
                             "16. Sum of vector values",
                             "17. Product of vector values",
                             "18. Average of vector values",
                             "19. Minimum of vector values",
                             "20. Maximum of vector values",
                             "q. Quit"]
        self.vectors = VectorRepository([MyVector(1, "r", 1, [2, 2, 2]),
                                         MyVector(2, "b", 2, [4, 0, 1]),
                                         MyVector(3, "g", 3, [7, 2, 8]),
                                         MyVector(4, "y", 4, [1, 5, 12])])

    def print_menu(self):
        for op in self.menu_options:
            print(op)

    def read_vector_info(self):
        while True:
            try:
                name_id = int(input("id = "))
                colour = input("colour = ")
                type = int(input("type = "))
                values = list(map(int, input("values = ").split()))
                return name_id, colour, type, values
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def run(self):
        while True:
            self.print_menu()
            print(self.vectors)
            option = input("option: ")
            try:
                match option:
                    case "1":
                        vector_info = self.read_vector_info()
                        self.vectors.add_vector(MyVector(*vector_info))
                    case "2":
                        print(self.vectors.vectors)
                    case "3":
                        index = int(input("index = "))
                        print(self.vectors.get_at_index(index))
                    case "4":
                        vector_id = int(input("id = "))
                        print(next((v for v in self.vectors.vectors if v.name_id == vector_id), None))
                    case "5":
                        index = int(input("index = "))
                        vector_info = self.read_vector_info()
                        self.vectors.update_vector(index, MyVector(*vector_info))
                    case "6":
                        vector_id = int(input("id = "))
                        vector_info = self.read_vector_info()
                        self.vectors.update_vector_by_id(vector_id, MyVector(*vector_info))
                    case "7":
                        index = int(input("index = "))
                        self.vectors.delete_by_index(index)
                    case "8":
                        vector_id = int(input("id = "))
                        self.vectors.delete_by_id(vector_id)
                    case "9":
                        self.vectors.plot_vectors()
                    case "10":
                        color = input("color = ")
                        print(self.vectors.sum_by_color(color))
                    case "11":
                        scalar = int(input("scalar = "))
                        self.vectors.add_scalar_to_all(scalar)
                    case "12":
                        index = int(input("index = "))
                        scalar = int(input("scalar = "))
                        self.vectors.get_at_index(index).add_scalar(scalar)
                    case "13":
                        index1 = int(input("index of first vector = "))
                        index2 = int(input("index of second vector = "))
                        self.vectors.get_at_index(index1).add(self.vectors.get_at_index(index2).values)
                    case "14":
                        index1 = int(input("index of first vector = "))
                        index2 = int(input("index of second vector = "))
                        self.vectors.get_at_index(index1).subtract(self.vectors.get_at_index(index2).values)
                    case "15":
                        index1 = int(input("index of first vector = "))
                        index2 = int(input("index of second vector = "))
                        result = self.vectors.get_at_index(index1).multiplication(self.vectors.get_at_index(index2).values)
                        print(f"Multiplication result: {result}")
                    case "16":
                        index = int(input("index = "))
                        print(f"Sum of vector values: {self.vectors.get_at_index(index).sum()}")
                    case "17":
                        index = int(input("index = "))
                        print(f"Product of vector values: {self.vectors.get_at_index(index).product()}")
                    case "18":
                        index = int(input("index = "))
                        print(f"Average of vector values: {self.vectors.get_at_index(index).average()}")
                    case "19":
                        index = int(input("index = "))
                        print(f"Minimum of vector values: {self.vectors.get_at_index(index).minimum()}")
                    case "20":
                        index = int(input("index = "))
                        print(f"Maximum of vector values: {self.vectors.get_at_index(index).maximum()}")
                    case "q":
                        break
                    case _:
                        print("Invalid option")
            except Exception as e:
                print(f"An error occurred: {e}")
