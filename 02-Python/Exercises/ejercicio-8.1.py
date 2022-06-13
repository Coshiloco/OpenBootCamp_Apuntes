# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

def main():
    f = open('mitextfile8.txt', 'w')
    f.write('Escribiendo en el archivo\n')
    f.close()

    f = open('mitextfile8.txt', 'r+')
    f.readline()
    f.write('Escribiendo en el archivo otra vez\n')

    f.seek(0)
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()
