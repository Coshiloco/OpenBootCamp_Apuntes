# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def esPrimo(num):
    if type(num) == float:
        print("No es un numero entero")
        return False

    for n in range(2, num):
        if num % n == 0:
            print(num, "No es primo", n, "es divisor")
            return False
    print(num, "Es primo")
    return True


esPrimo(5.6)
esPrimo(11)
esPrimo(89)
esPrimo(567)
esPrimo(1001)