# FUNCIONES
# Una función es un bloque de código que incluye instrucciones para realizar una taréa específica.


# def saludar(nombre, edad):
#     print("Hola " + nombre + " tienes " + edad + "años.")
#     print("Encantado de conocerte.")


# saludar("Dani,", "25 ")

# FUNCIONES LAMBDA
# Son funciones anónimas que se ejecutan en una línea, es decir, solo pueden tener una expresión.

# resultado = lambda numero: numero + 20
# print(resultado(30))
# suma = lambda numero1, numero2: numero1 + numero2
# print(suma(30, 60))

# RETURN
# La declaración Return nos permite recibir datos de una función.


def multiplicar_basica(numero1, numero2):
    return numero1 * numero2


res_multi_1 = multiplicar_basica(2, 5)
print(res_multi_1)


def multiplicar_dani(num1, num2):
    return num1 * num2


res_multi = multiplicar_dani(int(input()), int(input()))
print(res_multi)