# numero = 10
# numero1 = 5

# print(numero + numero1)
# print(numero - numero1)
# print(numero * numero1)
# print(numero / numero1)
# print(numero // numero1)
# print(numero ** numero1)

# resultado = 12 * 5 + 2 / 3 ** 2
# print(resultado)

# resultado2 = (12 * 5) + (2 / 3) ** 2
# print(resultado2)

# cadena1 = "Hola "
# cadena2 = "mundo"

# cadenas_unidas = cadena1 + cadena2
# print(cadenas_unidas)

# cadenas_repetidas = cadena1 * 3
# print(cadenas_repetidas)

numero1 = 10
numero2 = 5
numero3 = 10.0
numero4 = -10
numero5 = 5
numero_cadena = "10"

igual = numero1 == numero2
# print(igual)
igual = numero2 == numero5
# print(igual)
igual = numero2 == numero3
# print(igual)
igual = numero1 == numero_cadena
# print(igual)
igual = numero1 == numero4
# print(igual)

distinto = numero1 != numero2
#  print(distinto)

mayor_que = numero1 > numero2
# print(mayor_que)
mayor_que = numero1 > numero3
# print(mayor_que)

menor_que = numero1 < numero2
# print(menor_que)
menor_que = numero1 < int(numero_cadena)
# print(menor_que)

mayor_igual = numero1 >= numero3
# print(mayor_igual)

menor_igual = numero1 <= numero3
# print(menor_igual)

numero1 = 1
numero2 = 2

# Asignación suma
#  numero1 = numero1 + numero2
# print(numero1)
# numero1 = 1
# numero1 += numero2
# print(numero1)

# Asignación resta
# numero1 = numero1 - numero2
# print(numero1)
# numero1 = 1
# numero1 -= numero2
# print(numero1)

# Asignación multlipicación
"""
numero1 = numero1 * numero2
print(numero1)
numero1 = 1
numero1 *= numero2
print(numero1)
"""

# Asignación división
"""
numero1 = numero1 / numero2
print(numero1)
numero1 = 1
numero1 /= numero2
print(numero1)
"""

# Asignación exponente
"""
numero1 = numero1 ** numero2
print(numero1)
numero1 = 1
numero1 **= numero2
print(numero1)
"""

# Asignación división entera
"""
numero1 = numero1 // numero2
print(numero1)
numero1 = 1
numero1 //= numero2
print(numero1)
"""

# Asignación módulo o resto
"""
numero1 = numero1 % numero2
print(numero1)
numero1 = 1
numero1 %= numero2
print(numero1)
"""

# Reglas de precedencia en las operaciones matemáticas
"""
En orden de precedencia
1. Parentesis
2. Exponente
3. Multiplicación
4. División
5. Suma
6. Resta
"""

a = 1
b = 2

a, b = b, a + b
# print(a, b)

a = 1
b = 2

a = b
b = a + b
# print(a, b)

# Operadores lógicos
"""
or -> a or b -> ¿Se cumplen a o b?
and -> a and b -> ¿Se cumplen a y b?
not -> not x -> contrario de x
1 es verdadero
0 es falso
"""
verdadero = True
falso = False
# print("Comparador OR:")
# print(verdadero or falso, "\n")
# print("Comparador AND:")
# print(verdadero and falso)

# Operadores de pertenencia
# Evaluan si un objeto se encuentra dentro de otro

"""
in -> ¿Se encuentra en?
not in -> ¿No se encuentra en?
"""
cadena = "Hola mundo"
# print("H" in cadena)
# print("H " not in cadena)

# Operadores de identidad
# Sirven para comprobar si un objeto es igual o no a otro objeto
"""
is 
is not
"""
a = 10
b = 10

# print(a is b)
# print(a is not b)

# print(type(a) is int)
# print(a is not float)


nombres = ["Dani", "Sara"]    # Para crear listas
# print(nombres)
nombres.append("Myriam")      # Sirve para añadir otro nombre a la lista ya creada.
# print(nombres)

# Las cadenas pueden tratarse como listas, se pueden consultar como vemos abajo, pero no modificar como en las listas.
cadena = "Hola AcademiaCoder"

# H o l a   A c a d e m  i  a  C  o  d  e  r
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

letra = cadena[5]       # Eligiendo el orden de la letra de izquierda a derecha
# print(letra)

letra = cadena[-18]     # Eligiendo el orden de la letra de derecha a izquierda
# print(letra)

letras = cadena[2:13]
# print(letras)
letras = cadena[2:]
# print(letras)
letras = cadena[:13]
# print(letras)

modificada = cadena.capitalize()  # Primera letra en mayúscula
# print(modificada)

modificada = cadena.lower() # Todas las letras en minúscula
# print(modificada)

modificada = cadena.upper()
# print(modificada)

# Para comprobar si es cierto o no ponemos is.
modificada = cadena.isupper()
# print(modificada)

# Para concatenar cadenas lo ponemos seguido.
modificada = cadena.upper().isupper()
# print(modificada)

# Para que nos cree una lista con las palabras separadas por espacios usamos esta función.
modificada = cadena.split()
# print(modificada)

# Para acceder a una de esas palabras en concreto usamos esto:
modificada = cadena.split()
# print(modificada[0])

modificada = cadena.split()
# print(modificada[1])

# split separa por espacios en blanco, a no se que le especifiquemos por que queremos separar.
# Ejemplo:
cadena_con_comas = "Dani,Sara,Myriam,Noa"
lista_nombres = cadena_con_comas.split(",")
# print(lista_nombres)

# UNIENDO VARIABLES Y CADENAS
alumnos = 2500
academia = "AcademiaCoder"

cadena = "Los " + str(alumnos) + " alumnos de " + academia + " son muy aplicados"
# print(cadena)

# Otra forma de hacer esto pero más facil es con .format
cadena = "Los {} alumnos de {} son muy aplicados".format(alumnos, academia)
# print(cadena)

# Con la misma función pero sin necesidad de que esté ordenado se puede hacer así:
cadena = "Los {a} alumnos de {b} son muy aplicados".format(a=alumnos, b=academia)
# print(cadena

# Otra forma mucho más rápida y ordenada es la siguiente:
cadena = f"Los {alumnos} alumnos de {academia} son muy aplicados"
# print(cadena)

# INTRODUCIR TEXTO POR TECLADO
# Esta función es input()

# print("Indique su nombre:")
# nombre = input()
# print(f"Hola {nombre}, encantado de conocerte")

# Otra forma más simple es la siguiente:
nombre = input("Indica su nombre: ")
print(f"Hola {nombre}, encantado de conocerte")
años = input("¿Cuantos años tienes? ")

