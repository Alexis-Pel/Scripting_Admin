def user_input():
    """
        Function that retrieves a character string from a user.
        :param: None
        :return: user_string
    """
    user_string: str = input("Put your character")

    if not user_string.isascii():
        print("Character not supported, change it !")
        user_input()

    return user_string
