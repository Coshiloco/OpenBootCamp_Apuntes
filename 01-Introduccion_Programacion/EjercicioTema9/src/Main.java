//Ejercicio Tema 9
//----------------
//Crea una clase Persona con las siguientes variables:
//    La edad
//    El nombre
//    El teléfono
//Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.
//Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el teléfono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.
//Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador.

public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.setNombre("Alfredo");
        cliente.setEdad(36);
        cliente.setTelefono(600606060);
        cliente.setCredito(5000);

        Trabajador trabajador = new Trabajador();
        trabajador.setNombre("Luis");
        trabajador.setEdad(54);
        trabajador.setTelefono(677676767);
        trabajador.setSalario(2300);

        System.out.println(cliente.getNombre() + " " + cliente.getEdad() + " " + cliente.getTelefono() + " " + cliente.getCredito() );
        System.out.println(trabajador.getNombre() + " " + trabajador.getEdad() + " " + trabajador.getTelefono() + " " + trabajador.getSalario());
        }

   static class Persona {
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

   static class Cliente extends Persona {
        private int credito;

       public int getCredito() {
           return credito;
       }

       public void setCredito(int credito) {
           this.credito = credito;
       }
   }

   static class Trabajador extends Persona {
        private int salario;

        public int getSalario(){
            return salario;
        }

        public void setSalario(int salario) {
            this.salario = salario;
        }
   }
}