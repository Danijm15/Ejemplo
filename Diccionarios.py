# DICCIONARIOS
# Los diccionarios son una colección de datos no ordenada, pero que almacena sus datos utilizando una asignación (llave/identificador, valor).

# [] LISTAS - () TUPLAS - {} CONJUNTOS Y DICCIONARIOS

dias = {
    "lun": "Lunes",
    "mar": "Martes",
    "mie": "Miércoles",
    "jue": "Jueves",
    "vie": "Viernes",
    "sab": "Sábado",
    "dom": "Domingo"
}

print(dias)
# print(dias["lun"])
# print(dias["lll"])    # Con la forma básica de buscar, si algo no existe, me va a dar error en el código.

# print(dias.get("lll"))  # Con esta función para buscar, si algo no existe, me da un valor por defecto (None), en vez de darme error en el código.
# print(dias.get("lun"))
# print(dias.get("lll", "El identificador no existe")) # Podemos añadir a continuación lo que queramos que salga, en vez de None, cuando algo no existe.

# print(dias.pop("lun"))  # Elimina el valor que indiquemos del diccionario.
# print(dias)

# La función .update sirve para actualizar el diccionario.
dias.update(lun="Miercoles")    # De esta forma actualiza el valor de lun
print(dias)
dias.update(otro="Otro día")    # De esta forma, si no está el que busca, lo añade al final.While
print(dias)