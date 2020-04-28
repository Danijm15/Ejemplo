# TRATANDO CON ERRORES EN PYTHON

# try...except...else...finally

try:    # Intenta ejecutar lo que ponga debajo, si no hay error lo ejecuta y si hay algún error ejecuta hasta la línea por encima del error
    num1 = int(input("Ingresa un número: "))
    num2 = 0
    print(num1 /num2)
# Los dos errores que pueden haber son, por poner otra cosa que no sea un entero y por dividir entre 0.

except ZeroDivisionError as err:    # Va siempre con try y se ejecuta solo cuando hay error
    print(err)
except ValueError:
    print("Entrada invalida, debe ser un entero")
except:
    print("Vemos que subraya la palabra, por que habria que indicar que error puede dar, como en los dos de arriba")

else:   # Se ejecuta solo si no hay errores
    print("No hubo ningún error")

finally:    # Se ejecuta haya o no haya errores
    print("Se ejecuta siempre, sin importar que pase")