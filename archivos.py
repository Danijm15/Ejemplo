# ARCHIVOS

# Abrir y cerrar archivos

# Después de poner el nombre del archivo, indicamos que queremos hacaer con ese archivo.
# Ponemos r para leer (read), w para escribir (write), a para añadir (append), r+ para leer y esbrir.
# r solo lee el archivo, no puedes escribir. w solo puede escribir y no leer. a solo puede añadir y no leer.

"""
# Leer
archivo_estudiantes = open("estudiantes.txt", "r")    # Así abrimos un archivo
print(archivo_estudiantes)
print(archivo_estudiantes.readable())   # Esta función nos permite saber si el archivo está en modo de lectura
# print(archivo_estudiantes.read())       # Con esta función leemos el contenido
print(archivo_estudiantes.readline())   # Nos devuelve la primera línea
# print(archivo_estudiantes.readlines())  # Esta función nos devuelve el contenido del archivo en un array/lista
for estudiantes in archivo_estudiantes:
    print(estudiantes)
archivo_estudiantes.close()     # Así cerramos un archivo
# Una vez que python lee algo del archivo que hemos puesto, ya no lo puede leer, por que es como si python lo sacara del archivo, aunque en el archivo original
# siga estando. Si queremos leer algo dos veces tendriamos que volver abrir el archivo.
"""

"""
# Escribir y añadir
archivo_estudiantes2 = open("estudiantes.txt", "a")
print(archivo_estudiantes2)
# print(archivo_estudiantes2.writable())      # Esta función nos permite saber si el archivo está en modo de escribir
# print(archivo_estudiantes2.write("Este es un nuevo archivo\nY podemos hacer saltos de línea"))
print(archivo_estudiantes2.write("Eliah Jiménez - ReactJS"))
print(archivo_estudiantes2.write("\nNoa Jiménez - ReactJS"))    # Aquí añado el salto de línea por que no me habia dejado una línea en blanco al final en el archivo creado de estudiantes.
print(archivo_estudiantes2.write("\nAarón Jiménez - ReactJS"))
archivo_estudiantes2.close()
"""

# Eliminar un archivo
import os

os.remove("estudiantes2.txt")