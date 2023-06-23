"""
renombrar archivos
modificar permiso
eliminar archivo
"""
import csv
import shutil
import os

directorio_actual =os.getcwd 
print(directorio_actual)


archivo_original = r"C:\proyect_final\chatbot\modules\archivo.csv"
archivo_nuevo = r"C:\proyect_final\chatbot\modulesarchivo12.csv"

#def renombrar_archivos(archivo_original, archivo_nuevo):
shutil.move(archivo_original, archivo_nuevo)

#renombrar_archivos(archivo_original, archivo_nuevo)