from domain.Passenger import Passenger


class PassengerValidator:
    @staticmethod
    def validate(passenger: Passenger):
        """
        Validates a passenger object.
        :param passenger:
        :return:
        """
        if not isinstance(passenger, Passenger):
            raise TypeError("The object to validate must be an instance of Passenger.")

        errors = []

        if not passenger.first_name:
            errors.append("First name must not be empty.")

        if not passenger.last_name:
            errors.append("Last name must not be empty.")

        if not passenger.passport_number or passenger.passport_number <= 0:
            errors.append("Passport number must not be empty or negative.")

        if errors:
            raise ValueError("Validation errors: " + "; ".join(errors))
