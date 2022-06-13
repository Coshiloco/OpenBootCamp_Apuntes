# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle


class Vehiculo:
    nombre = ''
    cilindrada = 0
    cv = 0
    combustible = ''

    def __init__(self, nombre, cilindrada, cv, combustible):
        self.nombre = nombre
        self.cilindrada = cilindrada
        self.cv = cv
        self.combustible = combustible

    def getNombre(self):
        return self.nombre

def main():

    v = Vehiculo('Porsche', 3600, 450, 'Gasolina')

    file = open('object8.bin', 'wb')
    pickle.dump(v, file)
    file.close()

    file = open('object8.bin', 'rb')
    vehiculoLoad = pickle.load(file)
    print(vehiculoLoad.getNombre())
    file.close()


if __name__ == '__main__':
    main()
