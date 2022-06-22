def detectorPrimos(minimo, maximo):
    primos = [0]
    for numero in range(2, maximo):
        for primo in primos:
            if numero % primo == 0:
                break
    else:
        primos.append(numero)
        for numero in primos:
            if numero < minimo:
                print("num", primos.index(numero))
                primos.remove(numero)
    return primos


print("Bienvenido a la calculadora de primos entre varios numeros")
numerosValidos = False
while not numerosValidos:
    try:
        numeroMenor = int(input("Dime el numero mas bajo que quieres que te diga \n"))
        numeroMayor = int(input("Dime el numero mas alto que queires que mire \n"))
        numerosValidos = True
    except:
        input("Error, no has puesto un numero :(\npulsa enter para volver a poner los numeros")

print(detectorPrimos(numeroMenor, numeroMayor))


# def primos(numMenor, numMayor):
#     n = 1
#     listaPrimos = []
#     itsPrimo = True
#     if numMenor >= numMayor:
#         print("El numero menor es mayor o igual al mayor, pon otros dos numeros")
#
#     while n < numMayor:
#         for d in range(2, numMayor + 1):
#             if n != d:
#                 if n % d == 0:
#                     itsPrimo = False
#                     continue
#         if n >= numMenor and itsPrimo:
#             listaPrimos.append(n)
#         n += 1
#         itsPrimo = True
#     return listaPrimos
#
# print("Bienvenido a la calculadora de primos")
# numeroMinimo = int(input("Dime un el numero por el que empezar a buscar"))
# numeroMaximo = int(input("Dime el numero en el que quieres dejar de buscar"))
# print(primos(numeroMinimo, numeroMaximo))

# subjects = ["Matematicas", "Fisica", "Quimica", "Programacion"]
# scores = []
#
# for subject in subjects:
#         score = input(f"Que has sacado en {subject}?")
#         scores.append(score)
# for i in range(len(subjects)):
#     print("en", subjects[i], "has sacado", scores[i])
