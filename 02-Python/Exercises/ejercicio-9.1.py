# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

listaPaises = []

while True:
    pais = input("Introduce un pais, para continuar deja el espacio vacio: ")

    if pais:
        listaPaises.append(pais)
        continue

    if not pais:
        break


filtered = set(listaPaises)
sortedList = sorted(filtered)

print(sortedList)
