# SENTENCIAS BREAK Y CONTINUE (CONTROLADORES DEL FLUJO/CICLO)

# Las sentencias break y continue nos permiten manejar el flujo de la información en un bucle.
# Break es para acabar el bucle donde queramos que corte.
# Continue es para que se salte una parte del bucle y continue.

dias = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo"
]

for dia in dias:
    if dia == "Jueves":
        break
    print(dia)

print()

for dia in dias:
    if dia == "Jueves":
        continue
    print(dia)

print()

for indice in range(10):
    if indice == 5:
        break
    print(indice)

print()

for indice in range(10):
    if indice == 5:
        continue
    print(indice)