# CALCULADORA 2.0

num1 = float(input("Ingresa el primer número: "))
operador = input("Di que operación quieres realizar: ")
num2 = float(input("Ingresa el segundo número: "))

if operador == "+":
    resultado = num1 + num2
    print("La suma es:", resultado)
elif operador == "-":
    resultado = num1 - num2
    print("La resta es:", resultado)
elif operador == "*":
    resultado = num1 * num2
    print("La multiplicación es:", resultado)
elif operador == "/":
    resultado = num1 / num2
    print("La división es:", resultado)
elif operador == "**":
    resultado = num1 ** num2
    print("El exponente es:", resultado)
else:
    print("Error de operación.")