def leap_year():
    """
    Function that get a user input, if it's a year, it print if it's a leap year or not
    :param: None
    :return:
    """
    while True:
        user_input: str = input("Please enter a year or [x] for exit : ")
        if user_input.isdigit():
            print(is_leap_year(int(user_input)))
        elif user_input == "x":
            break
        else:
            print("Incorrect Input")
    return


def is_leap_year(year: int):
    """
    :param year: Int: Year input
    :return: True or False if the year is leap
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


leap_year()
