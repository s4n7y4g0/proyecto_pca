"""
crear directorio
crear archivo
eliminar directorio
mover archivo
"""
import csv
import os
import shutil

archivo = r'./file.csv'

#class directory_operations:


def crear_archivo():
    archivo = open ('archivo1.csv', 'w')
    print('el archivo se ha creado')

# crear_archivo()


carpeta = ('C:\proyect_final\chatbot/carpeta_test1')
def crear_directorio():
    try:
        os.mkdir(carpeta)
    except OSError:
        print("La creación del directorio %s falló" % carpeta)
    else:
        print("Se ha creado el directorio: %s " % carpeta)

#crear_directorio()


dir_carpeta = 'C:\proyect_final\chatbot/carpeta_test'

def eliminar_carpeta_vacia():
    shutil.rmtree(dir_carpeta)

# eliminar_carpeta_vacia()

origen = 'C:\\proyect_final\\chatbot\\carpeta_test1\\archivo1.csv'
destino = 'C:\\proyect_final\\chatbot\\carpeta_test2\\archivo1.csv' 
def mover_archivo(origen, destino):
    shutil.move(origen, destino)

mover_archivo(origen, destino)