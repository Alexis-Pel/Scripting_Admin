def is_leap_year():
    """
    Function that get a user input, if it's a year, it print if it's a leap year or not
    :param: None
    :return: None
    """
    while True:
        year = input("Enter new date for testing if is a leap year or q for exit :\n")

        if year.isdigit():
            cast_year_to_string = int(year)
            is_leapyear = cast_year_to_string % 4 == 0 and (
                        cast_year_to_string % 100 != 0 or cast_year_to_string % 400 == 0)
            print(is_leapyear)
        if year == "q":
            break


is_leap_year()
