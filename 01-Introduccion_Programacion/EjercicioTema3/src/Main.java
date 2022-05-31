//Primera parte:
//  1.1-Llamar a la función en el main y darle valores.
//  1.2-Crear una función con tres parámetros que sean números que se suman entre sí.

//Segunda parte:
//    2.1-Crear una clase coche.
//    2.2-Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
//    2.3-Una función que incremente el número de puertas que tiene el coche.
//    2.4-Crear un objeto miCoche en el main y añadirle una puerta.
//    2.5-Mostrar el número de puertas que tiene el objeto.

public class Main {
    public static void main(String[] args) {
        // 1.2-Llamar a la función en el main y darle valores.
        System.out.println(suma(1, 4, 5 ));

        // 2.4-Crear un objeto miCoche en el main y añadirle una puerta.
        Coche miCoche = new Coche();
        miCoche.aumentarPuertas();

        // 2.5-Mostrar el número de puertas que tiene el objeto.
        System.out.println(miCoche.numeroPuertas);
    }
    // 1.1-Crear una función con tres parámetros que sean números que se suman entre sí.
    public static int suma(int a, int b, int c){
        int resultado;
        resultado = a + b + c;
        return resultado;
    }
}

// 2.1-Crear una clase coche.
class Coche {
    // 2.2-Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
    public int numeroPuertas = 0;
    // 2.3-Una función que incremente el número de puertas que tiene el coche.
    public void aumentarPuertas() {
        this.numeroPuertas++;
    }
}