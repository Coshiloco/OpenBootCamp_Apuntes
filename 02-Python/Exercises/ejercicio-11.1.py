# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero,
# la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
import sqlite3


def main():
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    alumnoSearch = input("Nombre del alumno que quieres buscar?")
    query = f"SELECT * FROM alumnos WHERE nombre='{alumnoSearch.capitalize()}'"

    data = cursor.execute(query)
    for row in data:
        print(row)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
