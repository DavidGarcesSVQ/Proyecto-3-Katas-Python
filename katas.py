
# ============================================================
# PROYECTO 3 - KATAS PYTHON
# Autor: David Garcés Carrasco
#
# Este archivo contiene las soluciones de los 40 ejercicios.
# Cada ejercicio está separado y encabezado por su enunciado.
# ============================================================

from functools import reduce


# ============================================================
# EJERCICIO 1
# Escribe una función que reciba una cadena de texto como
# parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben
# ser considerados.
# ============================================================

def frecuencia_letras(texto):
    frecuencias = {}

    for letra in texto.lower():
        if letra.isalpha():
            frecuencias[letra] = frecuencias.get(letra, 0) + 1

    return frecuencias


# ============================================================
# EJERCICIO 2
# Dada una lista de números, obtén una nueva lista con el
# doble de cada valor. Usa la función map().
# ============================================================

def duplicar_numeros(numeros):
    return list(map(lambda numero: numero * 2, numeros))


# ============================================================
# EJERCICIO 3
# Escribe una función que tome una lista de palabras y una
# palabra objetivo como parámetros. Debe devolver una lista
# con todas las palabras que contengan la palabra objetivo.
# ============================================================

def buscar_palabras(palabras, objetivo):
    return [palabra for palabra in palabras if objetivo.lower() in palabra.lower()]


# ============================================================
# EJERCICIO 4
# Genera una función que calcule la diferencia entre los
# valores de dos listas. Usa la función map().
# ============================================================

def diferencias_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        raise ValueError("Las dos listas deben tener la misma longitud.")

    return list(map(lambda a, b: a - b, lista1, lista2))


# ============================================================
# EJERCICIO 5
# Escribe una función que tome una lista de números y un
# valor opcional nota_aprobado (por defecto 5). Debe calcular
# la media y determinar si está aprobado o suspenso.
# Debe devolver una tupla con la media y el estado.
# ============================================================

def evaluar_nota(notas, nota_aprobado=5):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")

    media = sum(notas) / len(notas)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return (media, estado)


# ============================================================
# EJERCICIO 6
# Escribe una función que calcule el factorial de un número
# de manera recursiva.
# ============================================================

def factorial(numero):
    if numero < 0:
        raise ValueError("No existe factorial para números negativos.")

    # Caso base: el factorial de 0 y de 1 es 1.
    if numero <= 1:
        return 1

    # La función se llama a sí misma con un número menor.
    return numero * factorial(numero - 1)


# ============================================================
# EJERCICIO 7
# Genera una función que convierta una lista de tuplas
# a una lista de strings. Usa la función map().
# ============================================================

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: str(tupla), lista_tuplas))


# ============================================================
# EJERCICIO 8
# Escribe un programa que pida al usuario dos números e
# intente dividirlos. Si introduce un valor no numérico o
# intenta dividir por cero, debe manejar esas excepciones.
# ============================================================

def solicitar_division():
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))

        resultado = numero1 / numero2
        print("La división es:", resultado)

    except ValueError:
        print("Error: debes introducir valores numéricos.")

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")


# ============================================================
# EJERCICIO 9
# Escribe una función que tome una lista de nombres de
# mascotas y devuelva una nueva lista excluyendo las
# mascotas prohibidas en España.
# Usa la función filter().
# ============================================================

def filtrar_mascotas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón",
                  "Cocodrilo", "Oso"]

    return list(filter(
        lambda mascota: mascota not in prohibidas,
        mascotas
    ))


# ============================================================
# EJERCICIO 10
# Escribe una función que reciba una lista de números y
# calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.
# ============================================================

class ListaVaciaError(Exception):
    """Excepción personalizada para listas sin elementos."""
    pass


def calcular_promedio(numeros):
    if len(numeros) == 0:
        raise ListaVaciaError("No se puede calcular la media de una lista vacía.")

    return sum(numeros) / len(numeros)


# ============================================================
# EJERCICIO 11
# Escribe un programa que pida al usuario su edad. Si
# introduce un valor no numérico o fuera del rango esperado
# (menor que 0 o mayor que 120), debe manejar los errores.
# ============================================================

def solicitar_edad():
    try:
        edad = int(input("Introduce tu edad: "))

        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")

        print("Tu edad es:", edad)

    except ValueError as error:
        print("Edad no válida:", error)


# ============================================================
# EJERCICIO 12
# Genera una función que, al recibir una frase, devuelva
# una lista con la longitud de cada palabra. Usa map().
# ============================================================

def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))


# ============================================================
# EJERCICIO 13
# Genera una función que, para un conjunto de caracteres,
# devuelva una lista de tuplas con cada letra en mayúsculas
# y minúsculas. Las letras no pueden estar repetidas.
# Usa map().
# ============================================================

def mayusculas_minusculas(caracteres):
    caracteres_unicos = sorted(set(caracteres))

    return list(map(
        lambda letra: (letra.upper(), letra.lower()),
        caracteres_unicos
    ))


# ============================================================
# EJERCICIO 14
# Crea una función que retorne las palabras de una lista
# que comiencen con una letra en específico.
# Usa la función filter().
# ============================================================

def palabras_por_letra(palabras, letra):
    return list(filter(
        lambda palabra: palabra.lower().startswith(letra.lower()),
        palabras
    ))

# ============================================================
# EJERCICIO 15
# Crea una función lambda que sume 3 a cada número
# de una lista dada.
# ============================================================

sumar_tres = lambda numeros: list(map(lambda numero: numero + 3, numeros))


# ============================================================
# EJERCICIO 16
# Escribe una función que tome una cadena de texto y un
# número entero n y devuelva una lista de las palabras
# que sean más largas que n. Usa filter().
# ============================================================

def palabras_mas_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))


# ============================================================
# EJERCICIO 17
# Crea una función que tome una lista de dígitos y
# devuelva el número correspondiente.
# Ejemplo: [5, 7, 2] devuelve 572.
# Usa reduce().
# ============================================================

def digitos_a_numero(digitos):
    if not digitos:
        raise ValueError("La lista de dígitos no puede estar vacía.")

    if any(type(digito) is not int or digito < 0 or digito > 9
           for digito in digitos):
        raise ValueError("Todos los elementos deben ser dígitos entre 0 y 9.")

    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)


# ============================================================
# EJERCICIO 18
# Crea una lista de diccionarios con información de
# estudiantes (nombre, edad y calificación) y usa filter()
# para extraer a los estudiantes con calificación >= 90.
# ============================================================

def estudiantes_destacados():
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 22, "calificacion": 85},
        {"nombre": "Marta", "edad": 19, "calificacion": 92},
        {"nombre": "Carlos", "edad": 21, "calificacion": 78}
    ]

    destacados = list(filter(
        lambda estudiante: estudiante["calificacion"] >= 90,
        estudiantes
    ))

    return destacados


# ============================================================
# EJERCICIO 19
# Crea una función lambda que filtre los números impares
# de una lista dada.
# ============================================================

filtrar_impares = lambda numeros: list(filter(lambda numero: numero % 2 != 0, numeros))


# ============================================================
# EJERCICIO 20
# Para una lista con elementos de tipo integer y string,
# obtén una nueva lista solo con los valores int.
# Usa filter().
# ============================================================

def obtener_enteros(elementos):
    # type(elemento) is int evita considerar True y False como enteros.
    return list(filter(lambda elemento: type(elemento) is int, elementos))


# ============================================================
# EJERCICIO 21
# Crea una función que calcule el cubo de un número dado
# mediante una función lambda.
# ============================================================

cubo = lambda numero: numero ** 3


# ============================================================
# EJERCICIO 22
# Dada una lista numérica, obtén el producto total
# de los valores. Usa reduce().
# ============================================================

def producto_total(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")

    return reduce(lambda a, b: a * b, numeros)


# ============================================================
# EJERCICIO 23
# Concatena una lista de palabras.
# Usa la función reduce().
# ============================================================

def concatenar_palabras(palabras):
    if not palabras:
        return ""

    return reduce(lambda palabra1, palabra2: palabra1 + palabra2, palabras)


# ============================================================
# EJERCICIO 24
# Calcula la diferencia total en los valores de una lista.
# Usa la función reduce().
# ============================================================

def diferencia_total(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")

    # Reduce resta cada elemento al resultado acumulado.
    return reduce(lambda acumulado, numero: acumulado - numero, numeros)


# ============================================================
# EJERCICIO 25
# Crea una función que cuente el número de caracteres
# en una cadena de texto dada.
# ============================================================

def contar_caracteres(texto):
    return len(texto)


# ============================================================
# EJERCICIO 26
# Crea una función lambda que calcule el resto de la
# división entre dos números dados.
# ============================================================

resto_division = lambda numero1, numero2: numero1 % numero2


# ============================================================
# EJERCICIO 27
# Crea una función que calcule el promedio de una
# lista de números.
# ============================================================

def promedio_lista(numeros):
    if not numeros:
        raise ValueError("No se puede calcular el promedio de una lista vacía.")

    return sum(numeros) / len(numeros)


# ============================================================
# EJERCICIO 28
# Crea una función que busque y devuelva el primer
# elemento duplicado en una lista dada.
# ============================================================

def primer_duplicado(elementos):
    vistos = set()

    for elemento in elementos:
        if elemento in vistos:
            return elemento

        vistos.add(elemento)

    return None

# ============================================================
# EJERCICIO 29
# Crea una función que convierta una variable en una cadena
# de texto y enmascare todos los caracteres con '#',
# excepto los últimos cuatro.
# ============================================================

def enmascarar_datos(valor):
    texto = str(valor)

    # Calculamos cuántos caracteres deben sustituirse.
    caracteres_a_ocultar = max(0, len(texto) - 4)

    return "#" * caracteres_a_ocultar + texto[-4:]


# ============================================================
# EJERCICIO 30
# Crea una función que determine si dos palabras son
# anagramas, es decir, si están formadas por las mismas
# letras pero en diferente orden.
# ============================================================

def son_anagramas(palabra1, palabra2):
    # Eliminamos espacios y convertimos a minúsculas.
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    return sorted(palabra1) == sorted(palabra2)


# ============================================================
# EJERCICIO 31
# Crea una función que solicite al usuario ingresar una
# lista de nombres y luego un nombre para buscar en esa
# lista. Si el nombre está, indica que fue encontrado;
# de lo contrario, lanza una excepción.
# ============================================================

def buscar_nombre_usuario():
    nombres = input("Introduce varios nombres separados por comas: ")
    lista_nombres = [nombre.strip() for nombre in nombres.split(",")]

    nombre_buscar = input("¿Qué nombre quieres buscar?: ").strip()

    if nombre_buscar.lower() in [nombre.lower() for nombre in lista_nombres]:
        print("El nombre ha sido encontrado.")
    else:
        raise ValueError("El nombre no se encuentra en la lista.")


# ============================================================
# EJERCICIO 32
# Crea una función que tome un nombre completo y una lista
# de empleados, busque el nombre y devuelva su puesto.
# Si no se encuentra, devuelve un mensaje indicando que
# esa persona no trabaja aquí.
# ============================================================

def buscar_empleado(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return empleado["puesto"]

    return "Esta persona no trabaja aquí."


# ============================================================
# EJERCICIO 33
# Crea una función lambda que sume elementos
# correspondientes de dos listas dadas.
# ============================================================

sumar_listas = lambda lista1, lista2: list(map(
    lambda a, b: a + b,
    lista1,
    lista2
))


# ============================================================
# EJERCICIO 34
# Crea la clase Arbol.
# Debe tener un tronco y ramas como atributos.
# Métodos: crecer_tronco, nueva_rama, crecer_ramas,
# quitar_rama e info_arbol.
#
# Caso de uso:
# a. Crear un árbol.
# b. Hacer crecer el tronco.
# c. Añadir una rama.
# d. Hacer crecer todas las ramas.
# e. Añadir dos ramas.
# f. Retirar la rama de la posición 2.
# g. Obtener información del árbol.
# ============================================================

class Arbol:

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        if posicion < 0 or posicion >= len(self.ramas):
            raise IndexError("La posición de la rama no existe.")

        self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitud_ramas": self.ramas.copy()
        }


# Caso de uso del ejercicio 34.
arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()

# Las posiciones de las listas empiezan en 0.
# La posición 2 corresponde a la tercera rama.
arbol.quitar_rama(2)

informacion_arbol = arbol.info_arbol()


# ============================================================
# EJERCICIO 35
# Crea la clase UsuarioBanco.
# Debe representar a un usuario con nombre, saldo y cuenta
# corriente. Métodos: retirar_dinero, transferir_dinero
# y agregar_dinero.
#
# Caso de uso:
# a. Alicia empieza con 100 y Bob con 50.
# b. Agregar 20 a Bob.
# c. Transferir 80 de Bob a Alicia.
# d. Retirar 50 del saldo de Alicia.
# ============================================================

class UsuarioBanco:

    def __init__(self, nombre, saldo, cuenta_corriente):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")

        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if not self.cuenta_corriente:
            raise ValueError("El usuario no tiene cuenta corriente.")

        if cantidad > self.saldo:
            raise ValueError("No hay saldo suficiente.")

        self.saldo -= cantidad

    def transferir_dinero(self, destinatario, cantidad):
        if not self.cuenta_corriente or not destinatario.cuenta_corriente:
            raise ValueError("Ambos usuarios deben tener cuenta corriente.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self.saldo:
            raise ValueError("No hay saldo suficiente para la transferencia.")

        # Restamos el dinero al emisor y lo añadimos al destinatario.
        self.saldo -= cantidad
        destinatario.saldo += cantidad

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.saldo += cantidad


# Caso de uso del ejercicio 35.
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)
bob.transferir_dinero(alicia, 60)
alicia.retirar_dinero(50)

# He adaptado el importe que transfiere BOB a Alicia porque el enunciado solicita transferir más dinero del que Bob tiene disponible.

# ============================================================
# EJERCICIO 36
# Crea una función llamada procesar_texto.
# Debe procesar un texto según la opción especificada:
# contar_palabras, reemplazar_palabras o eliminar_palabra.
#
# La función procesar_texto recibirá el texto, una opción
# ("contar", "reemplazar", "eliminar") y argumentos variables.
# ============================================================

def contar_palabras(texto):
    frecuencias = {}

    for palabra in texto.split():
        palabra = palabra.lower()
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra_eliminar):
    palabras = texto.split()

    palabras_filtradas = [
        palabra for palabra in palabras
        if palabra.lower() != palabra_eliminar.lower()
    ]

    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *argumentos):

    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        if len(argumentos) != 2:
            raise ValueError("Debes indicar la palabra original y la nueva.")

        return reemplazar_palabras(texto, argumentos[0], argumentos[1])

    elif opcion == "eliminar":
        if len(argumentos) != 1:
            raise ValueError("Debes indicar la palabra que quieres eliminar.")

        return eliminar_palabra(texto, argumentos[0])

    else:
        raise ValueError("Opción no válida.")


# ============================================================
# EJERCICIO 37
# Genera un programa que indique si es de noche, de día
# o de tarde según la hora proporcionada por el usuario.
# ============================================================

def clasificar_hora(hora):
    if hora < 0 or hora > 23:
        raise ValueError("La hora debe estar entre 0 y 23.")

    if 6 <= hora < 12:
        return "día"
    elif 12 <= hora < 20:
        return "tarde"
    else:
        return "noche"


# ============================================================
# EJERCICIO 38
# Escribe un programa que determine qué calificación en
# texto tiene un alumno según su calificación numérica.
# 0-69: insuficiente.
# 70-79: bien.
# 80-89: muy bien.
# 90-100: excelente.
# ============================================================

def calificacion_texto(nota):
    if nota < 0 or nota > 100:
        raise ValueError("La nota debe estar entre 0 y 100.")

    if nota < 70:
        return "insuficiente"
    elif nota < 80:
        return "bien"
    elif nota < 90:
        return "muy bien"
    else:
        return "excelente"


# ============================================================
# EJERCICIO 39
# Escribe una función que tome dos parámetros:
# figura ("rectangulo", "circulo" o "triangulo") y datos
# (una tupla con los datos necesarios para calcular el área).
# ============================================================

import math


def calcular_area(figura, datos):

    if figura == "rectangulo":
        if len(datos) != 2:
            raise ValueError("El rectángulo necesita base y altura.")

        base, altura = datos
        return base * altura

    elif figura == "circulo":
        if len(datos) != 1:
            raise ValueError("El círculo necesita el radio.")

        radio = datos[0]
        return math.pi * radio ** 2

    elif figura == "triangulo":
        if len(datos) != 2:
            raise ValueError("El triángulo necesita base y altura.")

        base, altura = datos
        return (base * altura) / 2

    else:
        raise ValueError("Figura geométrica no reconocida.")


# ============================================================
# EJERCICIO 40
# Escribe un programa que determine el monto final de una
# compra en una tienda online después de aplicar un descuento.
# Debe solicitar el precio, preguntar si tiene cupón y, si
# lo tiene, solicitar su valor. Solo se aplica si es mayor
# que cero. Utiliza if, elif y else.
# ============================================================

def calcular_compra():
    try:
        precio = float(input("Introduce el precio original: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

        cupon = input("¿Tienes un cupón de descuento? (S/N): ").strip().lower()

        if cupon in ("s", "si", "sí"):
            descuento = float(input("Introduce el descuento en porcentaje: "))

            if descuento > 0 and descuento <= 100:
                precio_final = precio - (precio * descuento / 100)
                print("Descuento aplicado.")
            elif descuento == 0:
                precio_final = precio
                print("El cupón no aplica ningún descuento.")
            else:
                precio_final = precio
                print("El descuento no es válido.")

        elif cupon in ("n", "no"):
            precio_final = precio
            print("No se ha aplicado ningún descuento.")

        else:
            print("Respuesta no válida.")
            return

        print("El precio final es:", round(precio_final, 2), "€")

    except ValueError:
        print("Error: introduce un valor numérico válido.")


# ============================================================
# COMPROBACIÓN DE LOS EJERCICIOS
# Este bloque permite probar las funciones principales.
# ============================================================

if __name__ == "__main__":

    print("\n===== COMPROBACIÓN DE KATAS PYTHON =====\n")

    # Ejercicio 1
    print("1. Frecuencia de letras:",
          frecuencia_letras("Hola mundo"))

    # Ejercicio 2
    print("2. Duplicar números:",
          duplicar_numeros([1, 2, 3, 4]))

    # Ejercicio 3
    print("3. Buscar palabras:",
          buscar_palabras(["casa", "casamiento", "perro"], "casa"))

    # Ejercicio 4
    print("4. Diferencias:",
          diferencias_listas([10, 20, 30], [1, 2, 3]))

    # Ejercicio 5
    print("5. Evaluación de notas:",
          evaluar_nota([7, 8, 6]))

    # Ejercicio 6
    print("6. Factorial:",
          factorial(5))

    # Ejercicio 7
    print("7. Tuplas a strings:",
          tuplas_a_strings([(1, 2), ("a", "b")]))

    # Ejercicio 9
    print("9. Mascotas permitidas:",
          filtrar_mascotas(["Perro", "Tigre", "Gato", "Oso"]))

    # Ejercicio 10
    print("10. Promedio:",
          calcular_promedio([5, 7, 9]))

    # Ejercicio 12
    print("12. Longitud de palabras:",
          longitud_palabras("Python es divertido"))

    # Ejercicio 13
    print("13. Mayúsculas y minúsculas:",
          mayusculas_minusculas("aAbBc"))

    # Ejercicio 14
    print("14. Palabras por letra:",
          palabras_por_letra(["casa", "coche", "perro"], "c"))

    # Ejercicio 15
    print("15. Sumar tres:",
          sumar_tres([1, 2, 3]))

    # Ejercicio 16
    print("16. Palabras largas:",
          palabras_mas_largas("Python es un lenguaje interesante", 5))

    # Ejercicio 17
    print("17. Dígitos a número:",
          digitos_a_numero([5, 7, 2]))

    # Ejercicio 18
    print("18. Estudiantes destacados:",
          estudiantes_destacados())

    # Ejercicio 19
    print("19. Números impares:",
          filtrar_impares([1, 2, 3, 4, 5]))

    # Ejercicio 20
    print("20. Solo enteros:",
          obtener_enteros([1, "dos", 3, "cuatro", 5]))

    # Ejercicio 21
    print("21. Cubo:",
          cubo(3))

    # Ejercicio 22
    print("22. Producto total:",
          producto_total([2, 3, 4]))

    # Ejercicio 23
    print("23. Concatenar palabras:",
          concatenar_palabras(["Hola", " ", "mundo"]))

    # Ejercicio 24
    print("24. Diferencia total:",
          diferencia_total([20, 5, 3]))

    # Ejercicio 25
    print("25. Contar caracteres:",
          contar_caracteres("Python"))

    # Ejercicio 26
    print("26. Resto de división:",
          resto_division(10, 3))

    # Ejercicio 27
    print("27. Promedio:",
          promedio_lista([6, 8, 10]))

    # Ejercicio 28
    print("28. Primer duplicado:",
          primer_duplicado([1, 2, 3, 2, 4]))

    # Ejercicio 29
    print("29. Enmascarar datos:",
          enmascarar_datos("123456789"))

    # Ejercicio 30
    print("30. ¿Son anagramas?:",
          son_anagramas("roma", "amor"))

    # Ejercicio 32
    empleados = [
        {"nombre": "Ana García", "puesto": "Programadora"},
        {"nombre": "Luis Pérez", "puesto": "Diseñador"}
    ]
    print("32. Buscar empleado:",
          buscar_empleado("Ana García", empleados))

    # Ejercicio 33
    print("33. Sumar listas:",
          sumar_listas([1, 2, 3], [4, 5, 6]))

    # Ejercicio 34
    print("34. Información del árbol:",
          informacion_arbol)

    # Ejercicio 35
    print("35. Saldos bancarios:",
          alicia.saldo, bob.saldo)

    # Ejercicio 36
    texto_prueba = "Python es fácil y Python es útil"
    print("36. Contar palabras:",
          procesar_texto(texto_prueba, "contar"))
    print("36. Reemplazar palabras:",
          procesar_texto(texto_prueba, "reemplazar", "fácil", "genial"))
    print("36. Eliminar palabra:",
          procesar_texto(texto_prueba, "eliminar", "útil"))

    # Ejercicio 37
    print("37. Clasificar hora:",
          clasificar_hora(15))

    # Ejercicio 38
    print("38. Calificación:",
          calificacion_texto(85))

    # Ejercicio 39
    print("39. Área del rectángulo:",
          calcular_area("rectangulo", (5, 3)))

  
    # ==========================================
    # PRUEBAS INTERACTIVAS
    # ==========================================

    # Ejercicio 8: División
    print("\n--- EJERCICIO 8: DIVISIÓN ---")
    solicitar_division()

    # Ejercicio 11: Validar edad
    print("\n--- EJERCICIO 11: EDAD ---")
    solicitar_edad()

    # Ejercicio 31: Buscar nombre
    print("\n--- EJERCICIO 31: BUSCAR NOMBRE ---")
    try:
        buscar_nombre_usuario()
    except ValueError as error:
        print("Error:", error)

    # Ejercicio 40: Compra y descuento
    print("\n--- EJERCICIO 40: COMPRA ---")
    calcular_compra()


    print("\n===== FIN DE LAS COMPROBACIONES =====")