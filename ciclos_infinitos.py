# CICLOS INFINITOS

# Iniciamos un ciclo infinito

while True:     # Solicitamos al usuario 1 para continuar el ciclo y 2 para detener el ciclo
    print("Ingresa (1) para continuar el ciclo")
    print("Ingresa (2) para detener el ciclo")
    opcion = input("> ")

    if opcion == "1":
        print("GRACIAS, selecciona otra opción")
        print("---O---")
    elif opcion == "2":
        print("GRACIAS, has detenido el ciclo")
        break
