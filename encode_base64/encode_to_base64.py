import argparse
import logging
import sys

logging.basicConfig(level=logging.INFO)
parser = argparse.ArgumentParser()
parser.add_argument('-string',
                    dest='string',
                    help='String to encode to Base64',
                    type=str
                    )
args = parser.parse_args()


def print_base64_string(base64_string: str):
    """
    Print base64_string
    :param: str: base64_string
    :return: base64_string
    """
    return logging.info(base64_string)


def concatenate_all_characters_in_array_base64(array_of_base64_character: [str]):
    """
    concatenate all characters in a array of base64 character
    :param array_of_base64_character: [str]
    :return: base64_string: str
    """
    base64_string: str = ""
    for i in array_of_base64_character:
        base64_string += i
    return base64_string


def transforms_all_decimals_to_base64_characters(array_of_decimal_character: [str]):
    """
    transforms
    :param array_of_decimal_character: [str]
    :return: array_of_base64_character: [str]
    """
    array_base64_model: [str] = (
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
        "W",
        "X",
        "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u",
        "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/")
    array_of_base64_character: [str] = []
    for i in array_of_decimal_character:
        array_of_base64_character.append(array_base64_model[int(i)])

    return array_of_base64_character


def binary_list_to_string(binary_list: [str]):
    """
    Concatenate binary list to one string
    :param binary_list: [str]: list of 8-bits
    :return: string: str : list concatenated of binary
    """
    string: str = ""
    for binary in binary_list:
        string += binary
    return string


def string_to_decimal(string_list: [str]):
    """
    Convert ASCII string list to decimal
    :param string_list: [str] : ASCII list
    :return: decimal_list: [int]: list of ASCII decimal corresponding to string_list
    """
    decimal_list: [int] = []
    for character in string_list:
        decimal_list.append(ord(character))

    return decimal_list


def user_input():
    """
        Function that retrieves a character string from a user.
        :param: None
        :return: user_string
    """
    user_string: str = args.string

    if not user_string.isascii():
        logging.warning("Character not supported, change it !")
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
    :return: list_utf transformed to binary numbers:
    """

    for indice, number in enumerate(list_utf):
        list_utf[indice] = bin(number).replace("0b", "")
    return list_utf


def separate_binary_string_grouped_by_6_blocks(binary: str):
    """
    transforms a string (binary) into a group of 6 bytes
    :param binary: str
    :return: array_of_grouped_octets: []
    """

    # ---all variable global in this function---#
    count: int = 1
    array_of_grouped_octets: [str] = []
    result = ""
    modulo_of_length_binary: int = len(binary) % 6

    # ---condition for inserting zeros to have a string modulo 6---#
    if modulo_of_length_binary != 0:
        for i in range(6 - modulo_of_length_binary):
            binary += "0"

    # ---loop for grouped in 6 bytes--- #
    for i in binary:
        result += i

        # ---condition for insert 6 bytes to 1 string
        if count == 6:
            array_of_grouped_octets.append(result)
            result = ""
            count = 0

        count += 1

    return array_of_grouped_octets


def binary_to_binary_octal(list_utf: [str]):
    """
    Transform the binary numbers to some octal binary numbers
    :param list_utf:
    :return: list_utf transformed to octal binary numbers
    """

    for indice, number in enumerate(list_utf):
        while len(number) % 8 != 0:
            number = "0" + number
        list_utf[indice] = number
    return list_utf


def binary_to_decimal_base64(list_base64: [str]):
    """
    Transform the binary numbers to decimal numbers
    :param list_base64:
    :return: list_base64 transformed to decimal numbers
    """

    for indice, number in enumerate(list_base64):
        list_base64[indice] = int(number, 2)
    return list_base64


if __name__ == "__main__":
    print_base64_string(__base64_string_completion(concatenate_all_characters_in_array_base64(
            transforms_all_decimals_to_base64_characters(binary_to_decimal_base64(
                separate_binary_string_grouped_by_6_blocks(binary_list_to_string(
                    binary_to_binary_octal(decimal_to_binary(string_to_decimal(user_input()))))))))))
    sys.exit(0)
