//Ejercicio Tema 8
//-----------------
//Crear clase Persona.
//Crear variables las privadas edad, nombre y teléfono de la clase Persona.
//Crear gets y sets de cada propiedad.
//Crear un objeto persona en el main.
//Utiliza los gets y sets para darle valores a las propiedades edad, nombre y teléfono, por último muéstralas por consola.

public class Main {
    public static void main(String[] args) {
        Persona persona = new Persona();
        persona.setEdad(36);
        persona.setNombre("Antonio");
        persona.setTelefono(656123456);
        System.out.println( persona.getNombre() + " " + persona.getEdad() + " " + persona.getTelefono());
    }

    public static class Persona {
        private int edad;
        private String nombre;
        private int telefono;

        public int getEdad() {
            return edad;
        }

        public void setEdad(int edad) {
            this.edad = edad;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public int getTelefono() {
            return telefono;
        }

        public void setTelefono(int telefono) {
            this.telefono = telefono;
        }
    }
}