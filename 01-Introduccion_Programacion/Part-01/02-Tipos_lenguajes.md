# Tipos de lenguajes de programación
---

- Que tipos de lenguajes de programación hay?

  - El primer tipo, son los lenguajes compilados, que significa compilados? Son lenguajes los cuales a partir de nuestro código se genera un programa que el procesador es capaz de ejecutar directamente a través del sistema operativo. El programa se crea, y usando una herramienta que se llama compilador lo transformamos en una secuencia de 0 y 1, que el procesador con la ayuda del sistema operativo es capaz de ejecutar. Se ejecuta Nativamente, el procesador es capaz de ejecutarlo. Ejemplos de lenguajes compilados: C, GO y ENSAMBLADOR.

  - El otro tipo de lenguaje son los lenguajes interpretados, un lenguaje interpretado también parte de un código origen, se pueden compilar a algo intermedio, este lenguaje intermedio se suele llamar BYTECODE, este intermedio el procesador no la entiende. ¿Para que este programa pueda ser ejecutado necesito un intérprete, que es un intérprete? Es un programa que lee el código y ejecuta paso a paso, pero no lo ejecuta directamente sobre el procesador, lo ejecuta sobre el mismo. Es mucho más lento que un lenguaje compilado. Ejemplo de lenguajes interpretados: JAVA, PYTHON, PEARL, PHP...

  - Diferencias entre compilado e interpretado, el compilado va mucho más rápido;  sin embargo, se necesita un compilador que sea capaz de generar una secuencia de unos y ceros acordes a nuestro procesador. Los procesadores tienen algo que se llama Arquitectura, la arquitectura tiene una cosa que se llama ISA, que hace que la secuencia de unos y ceros de un procesador Intel sea diferente a la de un procesador AMD, y que no es para nada igual a la de un móvil que es arquitectura ARM. Por cada programa que hago, tengo que compilarlo para cada procesador. Los interpretados por contra son más lentos, pero en este caso lo escribo una sola vez y el intérprete se encarga de adaptarlo al procesador. El lema de JAVA era "Write once, run anywhere", escribelo una vez y ejecútalo donde quieras. Pro que la Java Virtual Machine esta adaptada para muchísimos procesadores.

  - Y entre estos dos existen los híbridos, que son lenguajes interpretados cuyo intérprete es capaz de compilarlo a código nativo según le haga falta. A esto se le llama compilador JIT o Just In Time, y lo que hace es que interpreta en cualquier plataforma y es capaz de compilar para ese procesador, si una parte de mí intérprete circula muchas veces, por una parte, del código, lo compila para que así el procesador lo ejecute.

- Además de estos tipos, también podemos separarlos en dos tipos más de lenguajes que son:

  - Los lenguajes de tipado, son aquellos en los que puedo almacenar datos, pero le tengo que decir a mí intérprete que tipo de dato es. Por ejemplo JAVA es tipado.

  - Los lenguajes no tipados, son aquellos que mi compilador o interprete es capaz de deducir que tipo de datos es. Por ejemplo, PHP no es tipado.

---

## Tipos de aplicaciones

- Habitualmente utilizamos 3 tipos de aplicaciones
- Las aplicaciones WEB
- Las aplicaciones de ESCRITORIO
- Las aplicaciones MÓVILES

- Con el tiempo desde que salieron las primeras aplicaciones gráficas, hemos ido evolucionando y tenemos unos modelos, prácticamente todos desarrollamos de la misma manera, se podría decir que podemos ir globalizando.

### Aplicaciones web

* Las aplicaciones web como primera capa, vamos a llamarlo la chapa y pintura, que sería lo que el usuario ve. A esto lo denominamos el Front-End, que tiene una aplicación Web, tiene código HTML, código CSS para hacerlo bonito, y JavaScript que es la que le da funcionalidad. Estos tres trabajan altamente cohesionados.

* Desde el Front-End y sin que el usuario lo vea, se hacen peticiones al Back-End, el Back-end es un servidor que contiene la información de nuestra aplicación WEB.

* Una aplicación Web siempre en la parte frontal lleva HTML, CSS y JavaScript. Y en el Back-end que tiene la información remota, puede estar escrito en uno o múltiples lenguajes de programación, JAVA, GO, PYTHON, etc.

### Aplicación de escritorio

* Las aplicaciones de escritorio son prácticamente iguales, la parte que vemos es con la que el usuario interactúa. Y la parte de atrás no la vemos.

* En este caso cambia como está programada, en este caso en Windows suelen estar programadas en .NET o C++ y en Mac suelen estar programadas en SWIFT, y en Linux en C o C++, dependiendo del entorno que usemos.

### Aplicación Móvil

* Es exactamente lo mismo, lo único que cambia entre las 3 aplicaciones? La lógica que utilizan y los lenguajes que se usan.

* En los móviles cambia un poco, ya que en los móviles utilizan solo la vista y las acciones. En cambio, en escritorio queremos ver el máximo de información posible.
