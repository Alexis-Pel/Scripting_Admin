# Transform the numbers on a list to their binary value

def decimal_to_binary(list_utf):
    for indice, number in enumerate(list_utf):
        list_utf[indice] = bin(number).replace("0b", "")
    return list_utf
