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
