"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    p

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    all_seats = ["A", "B", "C", "D"]

    for _ in range(number):
        yield all_seats[_ % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_letters = generate_seat_letters(number)
    row_number = 1

    for seat in seat_letters:
        yield f"{row_number}{seat}"
        if seat == "D":
            row_number += 2 if row_number == 12 else 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    assigned_seats = {}
    seats = generate_seats(len(passengers))
    for index, seat in enumerate(seats):
        assigned_seats[passengers[index]] = seat

    return assigned_seats


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        code = f"{seat}{flight_id}"
        yield code + "0" * (12 - len(code))
