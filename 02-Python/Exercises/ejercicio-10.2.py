from tkinter import *

master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Gato", "Perro", "Caballo", "Tigre"]:
    listbox.insert(END, item)
listbox.pack()
label = Label(text="Nombres de animales")
label.pack()
master.mainloop()
