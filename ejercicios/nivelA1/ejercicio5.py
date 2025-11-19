'''
Ejercicio 5 - Libreria os
Haz un script que ejecute estas acciones por pasos:
Directorio actual:
Muestra el directorio de trabajo actual con os.getcwd().
Crear carpeta:
Crea una nueva carpeta llamada "prueba_python" utilizando os.mkdir().
Listar archivos:
Muestra todos los archivos y carpetas en el directorio actual con os.listdir().

'''

import os


if __name__ == '__main__':

# Muestra el directorio de trabajo actual con os.getcwd().
    print(os.getcwd())
# Crea una nueva carpeta llamada "prueba_python" utilizando os.mkdir()
    print(os.listdir())
    os.mkdir('prueba_python')
    print(os.getcwd())
    print(os.listdir())