from domain.Plane import Plane

class PlaneValidator:
    @staticmethod
    def validate(plane: Plane):
        """
        Validates a plane object.
        :param plane:
        :return:
        """
        if not isinstance(plane, Plane):
            raise TypeError("The object to validate must be an instance of Plane.")

        errors = []

        if plane.number <= 0:
            errors.append("Plane number must be a positive integer.")

        if not plane.airline_company:
            errors.append("Airline company must not be empty.")

        if plane.number_of_seats <= 0:
            errors.append("Number of seats must be a positive integer.")

        if not plane.destination:
            errors.append("Destination must not be empty.")

        if errors:
            raise ValueError("Validation errors: " + "; ".join(errors))