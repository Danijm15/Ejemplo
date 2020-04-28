# ADIVINA EL NÚMERO 1.0

import random

# Generamos un número aleatorio.
adivida = random.randint(1, 10)

nombre = input("Hola, cómo te llamas?\n")

print("Muy bien " + nombre + " estoy pensando en un número del 1 al 10, adivínalo, tienes 3 oportunidades.")

num = int(input("Primer intento: "))

if num == adivida:
    print("GANASTE")
else:
    print("Casi, casi")

    print("\nTe quedan 2 intentos.")

    num = int(input("Segundo intento: "))

    if num == adivida:
        print("GANASTE")
    else:
        print("Casi, casi")

        print("\nTe queda 1 intento.")

    num = int(input("Tercer intento: "))

    if num == adivida:
        print("GANASTE")
    else:
        print("Que pringao, perdiste.")

