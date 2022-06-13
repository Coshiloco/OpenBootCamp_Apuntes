# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.
# Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis
# una operación para calcular el tiempo que queda de trabajo.

import time
print(time.localtime())

working = True

while working:
    if time.localtime().tm_hour == 19:
        working = False
        print("Es hora de irse a casa!")
        break
    else:
        print("Quedan:", 19 - time.localtime().tm_hour, "horas y", 60 - time.localtime().tm_min, "minutos")

    time.sleep(30)
