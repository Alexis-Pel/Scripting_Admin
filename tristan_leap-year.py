def bissextile():
    """
        Function that get a user input, if it's a year, it print if it's a leap year or not
        :param: None
        :return:
        """
    while True:
        annee = int(input("Choisissez une année "))
        if annee != "q":
            if (annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0):
                print("L'année est une année bissextile!")
            else:
                print("L'année n'est pas une année bissextile!")
        else:
            break
bissextile()
