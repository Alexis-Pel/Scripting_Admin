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
        for i in range(6-modulo_of_length_binary):
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


