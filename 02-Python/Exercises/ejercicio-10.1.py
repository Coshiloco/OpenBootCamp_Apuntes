from tkinter import *


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))


def reset():
    opcion.set(None)
    monitor.config(text="")


window = Tk()

opcion = IntVar()

Radiobutton(window, text="Opción 1", variable=opcion,
            value=1, command=seleccionar).pack()
Radiobutton(window, text="Opción 2", variable=opcion,
            value=2, command=seleccionar).pack()
Radiobutton(window, text="Opción 3", variable=opcion,
            value=3, command=seleccionar).pack()

monitor = Label(window)
monitor.pack()

Button(window, text="Reiniciar", command=reset).pack()

window.mainloop()
