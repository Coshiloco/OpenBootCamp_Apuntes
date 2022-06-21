package com.company;

public class Tipos {

    public static void main(String[] args) {

        // variables
        // tipo identificador = valor;
        // o
        // tipo indetificador;
        // identificador = valor;

        // Enteros
        byte number1 = 1;   // 1 byte
        short number2 = 2;  // 2 byte
        int number3 = 3;    // 4 byte
        long number4 = 4;   // 8 byte

        // Punto Flotante
        float decimal1 = 4.9f;  // Utilizaremos como refuerzo la f para indicar que es float
        double decimal2 = 9.99d;// Utilizaremos la d para indicar que es dobule

        // Character
        char  caracter1 = 'a';

        // Booleans
        boolean verdadero = true;
        boolean falso = false;

        // Todos los que estan arriba son tipos de datos primitivos, en java lo detectamos porque empiezan en minuscula. Y no pueden ser nulos.

        // Tipos Envoltorio - No son datos primitivos y si pueden ser nulos.

        // Cadenas de texto
        String nombre = "Alan";

        // Mas tipos envoltorio
        Integer numero = null;
        Long numero2 = 2L; // Podemos colocar una L mayuscula para indicar que es long.

    }
}
