# LISTAS
# Una lista es una colección de elementos, las listas están ordenadas y son mutables.

numeros = [15, 22, 7, 10, 8, 1, 20]
frutas = ["Melón", "Sandia", "Platano", "Melocotón", "Mango", "Uva"]
#             0        1          2           3         4        5         Lectura de derecha a izquierda
#            -6       -5         -4          -3        -2       -1         Lectura de izquierda a derecha
print(numeros)
print(frutas)
# print(frutas[0])
# print(frutas[-1 ])
# print(frutas[1:])
# print(frutas[:4])
# print(frutas[2:])
# print(frutas[1:5])#

# FUNCIONES DE LAS LISTAS
# https://docs.python.org/3/library/array.html
# list ,len, append, extend, insert, remove, clear, pop, index, count, sort, reverse, copy
# lista = list(("Hola", "Adios", 5))   # Creamos una lista, pero esto no es muy util
# print(lista)
# print(len(frutas))  # Para saber como es de larga o cuantos elementos tiene una lista. Las dos cosas es lo mismo.
# frutas.append("Coco")   # Añade un elemento más al final de la lista ya creada.
# print(frutas)
# frutas[1] = "Manzana"   # Modifica el elemento que yo elija dentro del corchete por otro.
# print(frutas)
# numeros.extend(frutas)  # Añade una lista a la otra.
# print(numeros)
# frutas.insert(2, "Pomelo")  # Añade en la posición del índice que indiquemos, otro elemento a la lista y desplaza el resto una posición a la derecha.
# print(frutas)
# frutas.remove("Uva")    # Elimina el elemento que indiquemos.
# print(frutas)
# frutas.clear()  # Elimina todo el contenido de la lista.
# print(frutas)
# frutas.pop()    # Elimina el último elemento de la lista.
# frutas.pop()
# print(frutas)
# print(frutas.index("Platano"))  # Localiza la posición del elemento de la lista que indiquemos.
# print(frutas.count("Sandia"))   # Nos indica/cuenta las veces que aparece el elemento que indiques en la lista.
# frutas.sort()   # Ordena alfabéticamente los elementos de la lista.
# numeros.sort()  # Ordena los números de menos a mayor.
# print(frutas)
# print(numeros)
# frutas.reverse()    # Da la vuelta a la lista.
# numeros.reverse()
# print(frutas)
# print(numeros)
frutas2 = frutas.copy() # Copia la lista en otro espacio de memoria diferente al original, lo que hace que pueda editar uno de los dos sin que haga los cambios en las dos listas.
print(id(frutas))
print(id(frutas2))
print(frutas)
print(frutas2)
frutas2[2] = "Piña"
print(frutas2)
print(frutas)

frutas3 = frutas    # Copia todo lo que tiene la lista, incluido el mismo espacio de memoria, lo que hace que si hago un cambio en cualquiera de las dos listas, tambien lo hace en la otra.
print(frutas)
frutas3[4] = "Pera"
print(id(frutas))
print(id(frutas3))
print(frutas)
print(frutas3)
