//Parte 1:
//  Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
//  Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
//Parte 2:
//  Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
//  Incrementar el valor de la variable en uno cada vez que se ejecute.
//  Mostrarlo por pantalla cada vez que se ejecute.
//Parte 3:
//  Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.
//Parte 4:
//  Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.
//Parte 5:
//  Por último, para el Switch, deberás crear la variable estación, y distintos case para las cuatro estaciones del año.
//  Dependiendo del valor de la variable estación se deberá mandar un mensaje por consola informando de la estación en la que está.
//  También habrá que poner un default para cuando el valor de la variable no sea una estación.

public class Main {
    public static void main(String[] args) {
       //Parte 1: IF
        int numeroIf = 3;
        if (numeroIf < 0) {
            System.out.println("El numero es negativo");
        } else if (numeroIf > 0) {
            System.out.println("El numero es postivo");
        } else {
           System.out.println("El numero es 0");
        }

        //Parte 2: WHILE
        int numeroWhile = 0;
        while (numeroWhile < 3) {
            System.out.println("NumeroWhile: " + numeroWhile);
            numeroWhile = numeroWhile + 1;
        }

        //Parte 3: DO WHILE
        int numeroDoWhile = 0;
        do {
            System.out.println("NumeroDoWhile: " + numeroDoWhile);
            numeroDoWhile = numeroDoWhile + 3;
        } while(numeroDoWhile < 3);

        //Parte 4: FOR
        for (int numeroFor = 0; numeroFor <= 3; numeroFor = numeroFor + 1) {
            System.out.println("NumeroFor: " + numeroFor);
        }

        //Parte 5: SWITCH
        String estacion = "INVIERNO";
        switch (estacion) {
            case "VERANO":
                System.out.println("La estación actual es VERANO");
                break;
            case "OTOÑO":
                System.out.println("La estación actual es OTOÑO");
                break;
            case "INVIERNO":
                System.out.println("La estación actual es INVIERNO");
                break;
            case "PRIMAVERA":
                System.out.println("La estación actual es PRIMAVERA");
                break;
            default:
                System.out.println("El valor introducido no es una estación");
        }
    }
}
