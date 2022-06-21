def bissextile(year):
    """
        Function that returns true or false on whether it is a leap year or not.
        :param: year
        :return: boolean
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    if bissextile(2023):
        print("L'année \n,{rr} est une année bissextile!")
    else:
        print("L'année n'est pas une année bissextile!")

