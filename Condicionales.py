# DECLARACIÓN IF (CONDICIONALES)
# Esta declaración condicional nos permite realizar una acción si una condición se cumple u otra acción en caso de que no se cumpla.
# if, elif, else
# SI, SINO SI, SINO
"""
Ejemplo real:

Voy a salir,

SI hace calor,
    saldré en camiseta

SINO SI hace frio,
    saldré abrigado

SINO SI está lloviendo,
    llevaré paraguas

SINO
    me quedaré en casa
"""


si_es_hombre = False
eres_alto = True

"""
print("ANTES DEL IF\n")

if si_es_hombre and eres_alto:
    print("Eres un hombre alto")
elif si_es_hombre and not eres_alto:
    print("Eres un hombre bajo")
elif not si_es_hombre and eres_alto:
    print("No eres un hombre, pero si eres alto")
else:
    print("No eres un hombre y tampoco eres alto")

print("\nDESPUES DEL IF")
"""

# UTILIZANDO CONDICIONALES Y COMPARADORES

"""
def mayor_edad(num):
    if num >= 18:
        return True
    else:
        return False


edad = input("Ingresa tu edad: ")

if mayor_edad(int(edad)):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
"""

"""


def numero_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


numero = numero_mayor(int(input("Ingresa primer número: ")), int(input("Ingresa segundo número: ")), int(input("Ingresa tercer número: ")),)
print("El número mayor es: ", numero)


"""
"""


def quien_mayor(Dani, Sara, Myriam):
    if Dani >= Sara and Dani >= Myriam:
        return Dani
    elif Sara >= Dani and Sara >= Myriam:
        return Sara
    else:
        return Myriam

edad = quien_mayor(int(input("Dani: ")), int(input("Sara: ")), int(input("Myriam: ")))
print("La edad mayor es:", edad)

"""


def menor_que(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3


numero = menor_que(int(input("Introduce el primer número: ")), int(input("Introduce el segundo número: ")), int(input("Introduce el tercer número: ")))
print("EL número menor es:", numero)