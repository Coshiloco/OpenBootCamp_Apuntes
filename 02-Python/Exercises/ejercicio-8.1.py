# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

def main():
    open('mitextfile.txt', 'x')

    file = open('mitextfile.txt', 'w')
    file.write('Escribiendo en el archivo')
    file.close()


if __name__ == '__main__':
    main()
