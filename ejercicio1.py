'''
Hacer un programa que lea o escriba un fichero según el valor de una variable “decision”:
Si decision = 0, escribe en un fichero la ruta actual (os.getcwd()).
Si decision = 1, lee el fichero y muestra por consola “La ruta actual es <ruta actual>”.
'''

import os

decision = 1

if decision == 0: 
    with open("ruta.txt", "w") as f:
        ruta = os.getcwd()
        f.write(ruta)
    print("Ruta escrita correctamente")
elif decision == 1:
    with open("ruta.txt", "r") as f:
        print(f.read())