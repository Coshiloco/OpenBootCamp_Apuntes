# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares
# de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce

lista = [4, 473, 124, 421, 976, 273]


def filtrado(x):
    if x % 2:
        return True
    return False


def suma(a, b):
    return a + b


listaFiltrada = filter(filtrado, lista)
resultado = reduce(suma, listaFiltrada)
print(resultado)
