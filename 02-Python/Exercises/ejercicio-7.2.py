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
