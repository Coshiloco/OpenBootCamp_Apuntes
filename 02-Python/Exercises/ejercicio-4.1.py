# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad: int = input('Hola Usuario, introduce tu edad: ')

if int(edad) < 18:
    print('Eres menor de edad')
else:
    print('Eres Mayor de edad')