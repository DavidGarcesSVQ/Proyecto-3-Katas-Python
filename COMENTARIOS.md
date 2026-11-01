
# PROYECTO 3 - KATAS PYTHON

**Alumno:** David Garcés Carrasco
**Proyecto:** Katas Python

## 1. Introducción

En este proyecto he trabajado diferentes ejercicios prácticos de Python con el objetivo de aplicar los conocimientos adquiridos durante el curso.

He desarrollado funciones, utilizado estructuras de datos, aplicado condicionales y bucles, gestionado excepciones y trabajado con programación orientada a objetos.

Además, he realizado diferentes pruebas para comprobar que las soluciones funcionan correctamente, tanto con datos válidos como ante determinadas situaciones de error.

## 2. Organización del proyecto

El proyecto está organizado en dos archivos:

- `katas.py`: contiene los 40 ejercicios resueltos, numerados y encabezados por sus respectivos enunciados.
- `COMENTARIOS.md`: contiene la explicación de los pasos seguidos y de los principales conceptos utilizados, así como las pruebas realizadas.

## 3. Conceptos y herramientas utilizados

### Tipos de datos y funciones incorporadas

He trabajado con números enteros, decimales, cadenas de texto, listas, tuplas, diccionarios y conjuntos.

También he utilizado funciones incorporadas como:

- `len()`: obtener la longitud de una cadena o colección.
- `sum()`: sumar los elementos de una lista.
- `sorted()`: ordenar elementos.
- `str()`: convertir un valor en texto.
- `type()`: comprobar el tipo de un dato.
- `range()`: generar secuencias numéricas.

### Estructuras de datos

He utilizado:

- Listas para almacenar colecciones de elementos.
- Tuplas para agrupar datos.
- Diccionarios para almacenar información mediante claves y valores.
- Conjuntos para trabajar con elementos únicos.

También he utilizado métodos como `append()`, `pop()`, `split()` y `replace()`.

### Condicionales y estructuras de iteración

He utilizado las estructuras `if`, `elif` y `else` para tomar decisiones según las condiciones de cada ejercicio.

También he trabajado con bucles `for` para recorrer listas, cadenas y otras estructuras de datos.

### Funciones

He creado funciones utilizando `def` para organizar el código y reutilizar operaciones.

También he utilizado funciones lambda para realizar operaciones sencillas y funciones recursivas para resolver el cálculo del factorial.

### map(), filter() y reduce()

He practicado tres herramientas importantes de Python:

- `map()`: aplica una operación a todos los elementos de una colección.
- `filter()`: selecciona los elementos que cumplen una condición.
- `reduce()`: combina los elementos de una colección para obtener un único resultado.

Para utilizar `reduce()` he importado esta función desde el módulo `functools`.

### Gestión de excepciones

He utilizado `try` y `except` para controlar errores que pueden producirse durante la ejecución.

Entre otros, he gestionado:

- Valores no numéricos.
- Divisiones entre cero.
- Listas vacías.
- Valores fuera de los rangos permitidos.
- Operaciones que no pueden realizarse.

También he creado una excepción personalizada para controlar el cálculo del promedio de una lista vacía.

### Programación orientada a objetos

He creado las clases `Arbol` y `UsuarioBanco`.

En ellas he utilizado:

- El método `__init__()` para inicializar los objetos.
- Atributos para almacenar sus características.
- Métodos para definir sus comportamientos.
- Validaciones para evitar operaciones incorrectas.

### Módulos

He utilizado los siguientes módulos:

- `functools`: para importar la función `reduce()`.
- `math`: para utilizar el valor de PI en el cálculo del área de un círculo.

## 4. Pasos seguidos durante el proyecto

1. He revisado los enunciados para identificar qué conocimientos se necesitaban en cada ejercicio.
2. He organizado las soluciones en funciones independientes para facilitar su comprensión y reutilización.
3. He utilizado las herramientas y métodos solicitados en cada enunciado.
4. He incorporado validaciones para controlar datos incorrectos y situaciones excepcionales.
5. He añadido comentarios explicativos en las partes del código que requieren una explicación adicional.
6. He creado casos de uso para comprobar el funcionamiento de las clases.
7. He preparado un bloque de comprobaciones para verificar los resultados de las funciones.
8. He realizado pruebas interactivas para comprobar el comportamiento de los ejercicios que necesitan introducir datos por teclado.
9. He revisado los resultados obtenidos y corregido los aspectos necesarios para asegurar el correcto funcionamiento del programa.

## 5. Consideraciones y adaptaciones realizadas

Durante el desarrollo he tenido en cuenta algunas particularidades de determinados ejercicios:

### Ejercicio 1. Frecuencia de letras

La función convierte el texto a minúsculas y contabiliza únicamente los caracteres alfabéticos, evitando incluir espacios y signos de puntuación en el recuento.

### Ejercicio 20. Filtrar números enteros

He utilizado `type(elemento) is int` para seleccionar exclusivamente los números enteros. De esta forma, también se evita considerar los valores booleanos (`True` y `False`) como números enteros.

### Ejercicio 34. Clase Arbol

He creado objetos de la clase `Arbol` y he comprobado el funcionamiento de sus métodos para aumentar la longitud del tronco, añadir ramas, hacerlas crecer y eliminar una rama.

### Ejercicio 35. Clase UsuarioBanco

He implementado las operaciones de ingreso, retirada y transferencia de dinero, incorporando validaciones para evitar realizar operaciones cuando el saldo disponible no es suficiente.

He adaptado el importe de la transferencia del ejemplo de 80 € a 60 €, porque el enunciado solicita transferir más dinero del que Bob tiene disponible. Bob comienza con 50 € y recibe un ingreso de 20 €, por lo que dispone de 70 € antes de realizar la transferencia.

Con la adaptación, la operación puede realizarse correctamente y se mantienen las validaciones de saldo.

### Ejercicio 36. Procesamiento de texto

He desarrollado una función que permite realizar distintas operaciones sobre una cadena de texto: contar palabras, reemplazar palabras y eliminar palabras indicadas.

### Ejercicio 40. Cálculo de compra y descuentos

He incorporado validaciones para comprobar que el precio y el porcentaje de descuento sean correctos.

También he adaptado la respuesta a la pregunta sobre el cupón para aceptar distintas formas de introducir una respuesta afirmativa o negativa, incluyendo mayúsculas, minúsculas y respuestas con o sin tilde.

De esta forma, se aceptan respuestas como `S`, `s`, `SI`, `si`, `SÍ`, `sí`, `N`, `n`, `NO` y `no`.

Además, se contemplan los casos en los que no se aplica descuento, el descuento es incorrecto o la respuesta introducida no es válida.

## 6. Pruebas realizadas

Para comprobar el funcionamiento del proyecto he realizado dos tipos de pruebas: comprobaciones automáticas de las funciones y pruebas interactivas de los ejercicios que necesitan introducir datos por teclado.

### 6.1. Comprobaciones automáticas

He preparado un bloque de código para ejecutar diferentes funciones con datos de ejemplo y comprobar que los resultados obtenidos son los esperados.

Los resultados de las comprobaciones han sido satisfactorios:

| Ejercicio | Comprobación                   | Resultado obtenido             |
| --------- | ------------------------------ | ------------------------------ |
| 1         | Frecuencia de letras           | Recuento correcto              |
| 2         | Duplicar números               | `[2, 4, 6, 8]`                 |
| 3         | Buscar palabras                | `['casa', 'casamiento']`       |
| 4         | Diferencias entre listas       | `[9, 18, 27]`                  |
| 5         | Evaluación de notas            | `(7.0, 'aprobado')`            |
| 6         | Factorial                      | `120`                          |
| 7         | Tuplas a cadenas               | Conversión correcta            |
| 9         | Filtrar mascotas               | `['Perro', 'Gato']`            |
| 10        | Calcular promedio              | `7.0`                          |
| 12        | Longitud de palabras           | `[6, 2, 9]`                    |
| 13        | Mayúsculas y minúsculas        | Tuplas generadas correctamente |
| 14        | Filtrar palabras por letra     | `['casa', 'coche']`            |
| 15        | Sumar tres                     | `[4, 5, 6]`                    |
| 16        | Filtrar palabras largas        | Selección correcta             |
| 17        | Convertir dígitos en número    | `572`                          |
| 18        | Filtrar estudiantes destacados | Selección correcta             |
| 19        | Filtrar números impares        | `[1, 3, 5]`                    |
| 20        | Filtrar números enteros        | `[1, 3, 5]`                    |
| 21        | Calcular cubo                  | `27`                           |
| 22        | Producto de números            | `24`                           |
| 23        | Concatenar palabras            | `Hola mundo`                   |
| 24        | Diferencia acumulada           | `12`                           |
| 25        | Contar caracteres              | `6`                            |
| 26        | Resto de división              | `1`                            |
| 27        | Calcular promedio              | `8.0`                          |
| 28        | Buscar primer duplicado        | `2`                            |
| 29        | Enmascarar datos               | `#####6789`                    |
| 30        | Comprobar anagramas            | `True`                         |
| 32        | Buscar empleado                | `Programadora`                 |
| 33        | Sumar elementos de dos listas  | `[5, 7, 9]`                    |
| 34        | Información del árbol          | Tronco: 2; ramas: 2            |
| 35        | Saldos bancarios               | Alicia: 110 €; Bob: 10 €       |
| 36        | Procesamiento de texto         | Resultados correctos           |
| 37        | Clasificar hora                | `tarde`                        |
| 38        | Clasificar calificación        | `muy bien`                     |
| 39        | Calcular área de rectángulo    | `15`                           |

Los ejercicios 8, 11, 31 y 40 no aparecen en esta tabla porque necesitan introducir datos durante la ejecución y se han comprobado mediante pruebas interactivas.

### 6.2. Pruebas interactivas

He ejecutado también pruebas introduciendo datos directamente por teclado para comprobar el funcionamiento de los siguientes ejercicios:

**Ejercicio 8. División de dos números**

- Introducción de dos valores numéricos.
- Comprobación del resultado de la división.
- Control de la división entre cero.
- Control de entradas que no son numéricas.

**Ejercicio 11. Validación de edad**

- Introducción de una edad válida.
- Comprobación de valores negativos.
- Comprobación de edades superiores al límite establecido.
- Control de entradas no numéricas.

**Ejercicio 31. Búsqueda de nombres**

- Introducción de una lista de nombres separados por comas.
- Búsqueda de un nombre existente.
- Comprobación del comportamiento cuando el nombre no se encuentra.

**Ejercicio 40. Cálculo de compra y descuentos**

- Introducción del precio de un producto.
- Aplicación de un descuento mediante cupón.
- Comprobación de respuestas afirmativas y negativas.
- Comprobación de descuentos del 0 % y de porcentajes no válidos.
- Control de respuestas incorrectas y valores no numéricos.

Todas las pruebas interactivas se han ejecutado correctamente y han producido los resultados esperados.

### 6.3. Resultado general de las pruebas

Las comprobaciones automáticas y las pruebas interactivas han finalizado satisfactoriamente.

He verificado que las funciones principales devuelven los resultados esperados y que las validaciones y el tratamiento de excepciones funcionan correctamente en los casos comprobados.

## 7. Buenas prácticas aplicadas

Durante el desarrollo he intentado aplicar las siguientes buenas prácticas:

- Utilizar nombres de variables y funciones descriptivos.
- Separar las operaciones en funciones independientes.
- Evitar repetir código innecesariamente.
- Validar los datos antes de realizar determinadas operaciones.
- Utilizar comentarios para explicar los pasos importantes.
- Mantener una estructura ordenada y facilitar la lectura del código.
- Controlar los posibles errores para evitar interrupciones inesperadas.
- Comprobar el funcionamiento del código mediante diferentes casos de prueba.

