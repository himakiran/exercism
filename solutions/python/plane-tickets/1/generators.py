"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_list=['A','B','C','D']
    count=0
    while count<number:
        print(count)
        yield seat_list[count%4]
        count+=1


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
    seats=1
    row_num=1
    seat_letter = generate_seat_letters(number)
    while seats<=number:
        yield str(row_num)+next(seat_letter)
        seats+=1
        if (seats>4 and seats%4==1):
            row_num+=1
        if row_num==13:
            row_num=14
        

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_nums = generate_seats(len(passengers))
    seat_list={}
    for each in passengers:
        seat_list[each]=next(seat_nums)
    return seat_list

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for each in seat_numbers:
        yield each+flight_id+'0'*(12-(len(each)+len(flight_id)))
