# CLASES Y OBJETOS


class Estudiante:                                           # Definimos la clase poniendole el nombre que queremos
    def __init__(self, nombre, edad, curso_inicial):        # Con esta función inicializamos la clase y ponemos los atributos que vamos a utilizar
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.inscrito = True
        self.cursos = [curso_inicial]
                                                            # MÉTODOS DE LAS CLASES
    def desactivar(self):                                   # Definimos la función
        self.inscrito = False

    def suma(self, cursos):
        self.cursos.append(cursos)


estudiante1 = Estudiante("Dani", 25, "Python")              # Cada estudiante que creemos es el objeto

print(estudiante1.cursos)

curso1 = "HTTML"
curso2 = "Java"
curso3 = "C++"
cursos = [curso1, curso2, curso3]

estudiante1.suma(cursos)

print(estudiante1.cursos)

# estudiante1.edad = 26                                       # Aquí podemos cambiar la edad anterior

# print(estudiante1.nombre)                                   # No se puede imprimir la clase completa, si no, cada atributo

print(estudiante1.inscrito)

estudiante1.desactivar()                                      # El método de la función creada

print(estudiante1.inscrito)



"""
Esta clase podriamos importarla en otro archivo donde la necesitemos, sin necesidad de volverla a crear.
Sería de la siguiente manera.

from clases_objetos import Estudiante

"""
