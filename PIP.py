# PIP
# Gestor de paquetes, gestor de módulos o librerias creadas por terceros

# Los comandos se introducen por consola

"""
pip3 --version  # Para ver la version de pip3 que tenemos
pip3 install python-docx    # Para instalar la libreria que queremos

from docx import Document

document = Document()

pip3 list # Para ver los archivos que tiene instalado pip y que hacen falta para usar alguna libreria instalada
pip3 freeze # Para ver los archivos que tiene instalado pip y que hacen falta para usar alguna libreria instalada
pip3 freeze > requirements.txt  # Para crear un archivo con los requisitos para que una libreria funcione correctamente
pip3 install -r requirements.txt    # Para instralar los archivos que requiere una libreria para su correcto funcionamiento
pip3 uninstall python-docx  # Para desinstalar la libreria que ya no necesitemos.
"""
