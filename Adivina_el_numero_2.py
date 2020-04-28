# ADIVINA EL NÚMERO 2.0

import random

# Variables para modificar el juego
posibilidades = 5
limite = 20

nombre = input("Hola, cómo te llamas? \n")

print("Muy bien " + nombre.capitalize() + " estoy pensando en un número del 1 al " + str(limite) + ", adivinalo si puedes, tienes " + str(posibilidades) + " oportunidades.")


while True:

    # Generamos un número aleatorio entre 1 y 20
    adivina = random.randint(1, limite)
    intentos = 0
    while intentos < posibilidades:

        numero = int(input("\nIntenta adivinar el número: "))

        if numero == adivina:
            print("GANASTE.")
            print("---O---")
            print()
            break
        elif (intentos + 1) < posibilidades:
            if numero > adivina:
                print("Llevas " + str(intentos + 1) + " intentos")
                print("El número es más pequeño.")
            else:
                print("Llevas " + str(intentos + 1) + " intentos")
                print("El número es más grande.")

        intentos += 1

    if numero != adivina:


        print("\nPerdiste, el número era ", adivina)
        print("---O---\n")

    print("Si quieres volver a jugar pulsa (1)")
    print("Si quieres dejar de jugar pulsa (2)")
    opcion = input("> ")

    if opcion == "1":
        print("---O---\n")
    elif opcion == "2":
        print("\nHasta la próxima")
        break


