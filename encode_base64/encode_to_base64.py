def user_input():
    """
        Function that retrieves a character string from a user.
        :param: None
        :return: user_string
    """
    user_string: str = input("Put your character\n")

    if not user_string.isascii():
        print("Character not supported, change it !")
        user_input()

    return user_string


def list_user_input(user_string: str):
    """
    Function that transforms the character string into a list by character.
    :param: user_input
    :return:list_user_input
    """
    return list(user_string)


def __base64_string_completion(base64_string: str):
    """
    Complete base64_string with '='  : so that the encoder can be a byte
    :param base64_string: str: base64 String
    :return:
    """
    while (len(base64_string) % 8) != 0:
        base64_string += "="
    return base64_string


def decimal_to_binary(list_utf: [int]):
    """
    Transform the numbers on a list to their binary value
    :param list_utf:
    :return: list_utf transformés en nombres binaires
    """

    for indice, number in enumerate(list_utf):
        list_utf[indice] = bin(number).replace("0b", "")
    return list_utf
