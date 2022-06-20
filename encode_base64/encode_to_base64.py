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

def __base64_string_completion(base64_string: str):
    """
    Complete base64_string with '='  : so that the encoder can be a byte
    :param base64_string: str: base64 String
    :return:
    """
    while (len(base64_string) % 8) != 0:
        base64_string += "="
    return base64_string

