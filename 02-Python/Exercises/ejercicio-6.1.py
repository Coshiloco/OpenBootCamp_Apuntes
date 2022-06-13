# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas
#
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada
#
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    Color = "Verde"
    Ruedas = 5
    Puertas = 4


class Coche(Vehiculo):
    Velocidad = 170
    Cilindrada = 1600


c = Coche()

print(c)
print(c.Color)
print(c.Ruedas)
print(c.Puertas)
print(c.Velocidad)
print(c.Cilindrada)
