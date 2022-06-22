import logging
import sys
import argparse

logging.basicConfig(level=logging.INFO)
parser = argparse.ArgumentParser()
parser.add_argument('-year',
                    dest='year',
                    help='Year to test',
                    type=str,
                    nargs='+')
args = parser.parse_args()


def leap_year():
    """
    Function that sai if the user input, if it's a number, is a leap year or not
    :param: None
    :return:
    """
    user_input_list: str = args.year
    for user_input in user_input_list:
        if user_input.isdigit():
            logging.info(f"\n{user_input} is a leap year") if is_leap_year(int(user_input)) else logging.info(
                f"\n{user_input} is not a leap year")
        else:
            logging.warning("Incorrect Input")
    return


def is_leap_year(year: int):
    """
    :param year: Int: Year input:
    :return: True or False if the year is leap
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


if __name__ == "__main__":
    leap_year()
    sys.exit(0)
