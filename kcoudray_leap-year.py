print("Saisir une année")

year = int(input())

if year%4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("L'année est bissextile")
else:
    print("L'année n'est pas bissextile")
