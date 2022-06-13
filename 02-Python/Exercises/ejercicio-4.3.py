# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

numero = 100

while numero != 0:
    print(numero)
    numero -= 1


listaNumeros = []

for numeros in range(0,101):
    listaNumeros.append(numeros)

print(sorted(listaNumeros, reverse=True))