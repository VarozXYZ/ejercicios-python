'''
Crear una función que compare tres números recibidos como parámetros, e imprima por consola cuál es el número más alto.
'''

def comparador(a, b, c):
    lista = (a, b, c)
    num = a
    for i in lista:
        if num < i:
            num = i
    return num

print(f"El número más alto es: {comparador(100, 200, 20)}")