# Calculadora básica
numero1 = input("Primer número: ")
numero2 = input("Segundo número: ")


suma = float(numero1) + float(numero2)
resta = float(numero1) - float(numero2)
multiplicación = float(numero1) * float(numero2)
división = float(numero1) / float(numero2)

operación = float(input("Indica la operación a realizar: "))
if operación == 1:
    resultado = float(numero1) + float(numero2)
    print(resultado)
elif operación == 2:
    resultado = float(numero1) - float(numero2)
    print(resultado)
elif operación == 3:
    resultado = float(numero1) * float(numero2)
    print(resultado)
elif operación == 4:
    resultado = float(numero1) / float(numero2)
    print(resultado)




