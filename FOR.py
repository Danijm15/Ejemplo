# BUCLE FOR (Para)

# Nos permite recorrer una colección de valores.

for letra in "AcademiaCoder":
    print(letra, id(letra))

print(letra, id(letra))     # Luego esa variable sigue valiendo el último valor asignado y sigue estando en la última posición de memoria.
print()
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for dia in dias:
    print(dia)

print()

dias2 = {
    "lun": "Lunes",
    "mar": "Martes",
    "mie": "Miércoles",
    "jue": "Jueves",
    "vie": "Viernes",
    "sab": "Sábado",
    "dom": "Domingo"
}

for llave, clave in dias2.items():  # Esta función es para diccionarios, para imprimir la llave, la clave o ambas.
    print(llave)
    print(clave)
    print(llave, clave)

print()

for indice in range(5):     # Para ver el rango numérico de algo, o como en este caso, creamos un rando de 5 posiciones.
    print(indice)

print(range(5))

print()

for indice in range(10):
    if indice == 4:
        print("Ganaste")

    else:
        print("No ganaste")

print()

# Para anidar dos FOR, lo hacemos de la siguente manera:
for indice in range(5):
    for indice2 in range(3):
        print(indice, indice2)
