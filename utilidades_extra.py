import random

metros_en_kilometro = 1000
super_heroes = ["IronMan", "Capitán América", "Thor", "Hulk"]


def tomar_extension(filname):
    return filname[filname.index(".") + 1:]


def tirar_dado(num):
    return random.randint(1, num)

# Este archivo se genera para usarlo con el archivo MODULOS