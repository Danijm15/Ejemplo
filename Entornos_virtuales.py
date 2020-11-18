# ENTORNOS VIRTUALES
# SIRVEN PARA INSTALAR PAQUETES QUE VAYAMOS A USAR EN UN PROYECTO DETERMINANDO
# SIN TENER QUE INSTARLAR LOS PAQUETES EN TODOS LOS PROYECTOS


"""
pip3 install virtualenv     # Este comando se pone para instalarlo
pip3 list                   # Este comando se pone para que veamos que se ha instalado
pip3 freeze                 # Este comando es otra forma de ver lo mismo que el comando de arriba
virtualenv env              # Con este comando creamos el entorno virtual.
                            # El env del final es el nombre que le ponemos al entorno virtual, podemos ponerle el que queramos
cd env                      # Este comando es para entrar a la carpeta creada del entorno virtual
source bin/activate         # Este comando es para activar el entorno de trabajo
source env/bin/activate     # Este comando es para activarlo sin necesidad de entar en la carpeta previamente
pip list                    # Dentro del entorno virtual ya no se usa pip3 sino pip, es un atajo de teclado
deactivate                  # Con este comando se desactiva en entorno virtual

"""