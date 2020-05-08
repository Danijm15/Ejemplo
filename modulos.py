# MÓDULOS/LIBRERIAS

# Un módulo es un archivo que podemos importar dentro de un archivo en el cual
# estamos trabajando y hacer uso de su contenido, como funciones y variables.

"""
import utilidades_extra     # Para importar todo el archivo completo
print(utilidades_extra.metros_en_kilometro)
print(utilidades_extra.super_heroes)
print(utilidades_extra.super_heroes[0])
"""

"""
import utilidades_extra as ue       # Usamos as(como), para abreviar el nombre y que no se vea muy cargado el código
print(ue.tirar_dado(6))
print(ue.super_heroes)
"""

"""
from utilidades_extra import tirar_dado, super_heroes       # Si el archivo es muy grande, importamos solo lo que vamos a utilizar, para no hacerlo muy pesado.
print(tirar_dado(6))
print(super_heroes)
"""

"""
from utilidades_extra import tirar_dado as td
print(td(6)
"""

# TODAS LAS IMPORTACIONES QUE SE HAGAN, VAN ARRIBA DEL TODO
# LAS QUE SE HAGAN CON FROM, VAN LAS SEGUNDAS

import random
from utilidades_extra import tirar_dado as td

print(random.randint(10, 15))
  
print(td(6))


