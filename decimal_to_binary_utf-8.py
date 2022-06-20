def decimal_to_binary(list_utf: [int]):

    """
    Transform the numbers on a list to their binary value
    :param list_utf:
    :return: list_utf transformés en nombres binaires
    """

    for indice, number in enumerate(list_utf):
        list_utf[indice] = bin(number).replace("0b", "")
    return list_utf
