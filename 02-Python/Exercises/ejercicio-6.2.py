# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
# que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    nombre = ""
    nota = 0

    def setNota(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def getNota(self):
        print(self.nombre, self.nota)
        if self.nota >= 5:
            print("El alumno", self.nombre, "a aprovado")
        else:
            print("El alumno", self.nombre, "a suspendido")


a = Alumno()
a.setNota("Miguel Jimenez", 3)
a.getNota()
