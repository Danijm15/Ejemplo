# BÚSQUEDA BINARIA

lista = [0, 88, 72, 21, 14, 16, 90, 35, 47, 6, 68, 12, 10, 54, 41]

lista.sort()                                                            # Ordena la lista de menor a mayor

# 1. Buscamos el punto medio (puntero)
# 2. Comprobamos si el puntero es el valor que buscamos
# 3. Si el número es mayor al valor que buscamos, aumentamos inicio 1 sobre el puntero
# 4. Si el número es menor al valor que buscamos, disminuimos el final 1 baja el puntero
# 5. Si inicio mayor o igual que final, entonces el valor no se encuentra en la lista

def busqueda_binaria(valor):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        puntero = (inicio + final) // 2
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None


def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f"El número {valor} no se encontró"
    else:
        return f"El número {valor} se encuentra en la posición {res_busqueda}"


print("Ingresa un número:")
número = int(input())
print(buscar_valor(número))


while True:
    print("Si quiere seguir jugando pulse (1):")
    print("Si no quiere seguir jugando pulse (2):")
    opción = input("> ")
    if opción == "1":
        print("Sigue jugando.")
        print("---o---")
        print()
        print("Ingresa un número:")
        número = int(input())
        print(buscar_valor(número))
    elif opción == "2":
        print("Hasta pronto.")
        break

