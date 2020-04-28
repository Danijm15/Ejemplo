# ENCRIPTADOR DE FRASES

# "Hola AcademiaCoder, ¿Cómo están hoy?
# Caracter elegido "xX"
# Hxlx XcxdxmxxCxdxr, ¿Cxmx xstxn hxy?

"""
def encriptar(frase):
    encriptada = ""
    for letra in frase:
        if letra in "AEIOUÁÉÍÓÚaeiouáéíóú":
            if letra.isupper():
                encriptada = encriptada + "X"
            else:
                encriptada = encriptada + "x"
        else:
            encriptada = encriptada + letra
    return encriptada

print(encriptar(input("Ingresa una frase:\n> ")))
"""

# Variables para modificar el programa


while True:

    caracter_elegido = input("Elige la letra para la encriptación: ")
    acento_letra = input("Elige la letra para el acento: ")

    def encriptar(frase, caracter, acento):
        encriptada = ""
        for letra in frase:
            if letra.lower() in "aeiou":
                if letra.isupper():
                    encriptada = encriptada + caracter.upper()
                else:
                    encriptada = encriptada + caracter
            elif letra.lower() in "áéíóú":
                if letra.isupper():
                    encriptada = encriptada + acento.upper()
                else:
                    encriptada = encriptada + acento
            else:
                encriptada = encriptada + letra
        return encriptada



    print(encriptar(input("\nIngresa una frase:\n> "), caracter_elegido, acento_letra))

    print("---O---\n")
    print("Pulsa (1) para encriptar otra frase")
    print("Pulsa (2) para salir")
    opcion = input("> ")

    if opcion == "1":
        print("---O---\n")
    elif opcion == "2":
        print("\nHasta la próxima")
        break