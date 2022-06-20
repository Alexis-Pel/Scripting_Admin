
def is_LeapYear():
    """
    Function that get a user input, if it's a year, it print if it's a leap year or not
    :param: None
    :return: None
    """
    while True:
        year = input("Enter new date for testing if is a leap year or q for exit :\n")

        if year.isdigit():
            castYearToString = int(year)
            is_leapyear = castYearToString % 4 == 0 and (castYearToString % 100 != 0 or castYearToString % 400 == 0)
            print(is_leapyear)
        if year == "q":
            break

is_LeapYear()