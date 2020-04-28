# LISTAS ANIDADAS o LISTAS DE VARIAS DIMENSIONES

# Son listas que están dentro de otras listas

lista_numeros = [
    [1, 2, 3],      # Fila -> Horizontal
    [4, 5, 6],      # Columna -> Vertical
    [7, 8, 9],
    [0]
]

print(lista_numeros[1][1])

for numero in lista_numeros:
    print(numero)

for fila in lista_numeros:
    for columna in fila:
        print(columna)