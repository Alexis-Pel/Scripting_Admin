import sys

while True:
    print("Saisir une année")

    year = int(input())

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("L'année est bissextile")
    else:
        print("L'année n'est pas bissextile")

    print("Voulez vous continuer? Tapez Y si vous voulez taper une autre date ou alors n'importe quelle autre touche "
          "si vous voulez quitter")
    if input() != 'Y':
        sys.exit()
    else:
        continue
