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
