# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y
# otra función que calcule el área de un círculo recibiendo el radio del mismo.

def areatriangulo(altura, base):
    area = altura * base / 2
    print(area)


def areacirculo(radio):
    pi = 3.1415
    area = pi * radio**2
    print(round(area, 2))


areatriangulo(6, 3)
areacirculo(23)
