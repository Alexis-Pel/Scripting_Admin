import argparse

parser = argparse.ArgumentParser()
user_interface = argparse.ArgumentParser()
parser.add_argument('--year', type=int, help='year')
parser.add_argument('--u', type=str, help='u interface user')
args = parser.parse_args()


def is_leap_year():
    """
    Function that get a user input, if it's a year, it print if it's a leap year or not
    :param: None
    :return: None
    """
    if args.u == "true":
        while True:
            year = input("Enter new date for testing if is a leap year or q for exit :\n")
            if year.isdigit():
                cast_year_to_string = int(year)
                is_leapyear = cast_year_to_string % 4 == 0 and (
                        cast_year_to_string % 100 != 0 or cast_year_to_string % 400 == 0)
                print(is_leapyear)
            if year == "q":
                break

    else:
        cast_year_to_string = int(args.year)
        is_leapyear = cast_year_to_string % 4 == 0 and (
                cast_year_to_string % 100 != 0 or cast_year_to_string % 400 == 0)
        print(is_leapyear)


is_leap_year()
