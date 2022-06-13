# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "Es bisiesto")
    else:
        print(year, "No es bisiesto")


bisiesto(845)
bisiesto(896)
bisiesto(963)
bisiesto(2400)

