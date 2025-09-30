'''
Crear una función que reciba una lista de palabras como parámetro, e imprima por consola una tupla que contenga dos listas:
Cuáles de esas palabras contienen al menos una “a”.
Cuáles de esas palabras tienen al menos 5 letras.
'''

def tuplaPalabras(lista):
    a = []
    b = []
    for p in lista:
        if "a" in p:
            a.append(p)
        if len(p) >= 5:
            b.append(p)
    
    c = (a, b)
    
    print(f"Lista de palabras que contienen a: {c[0]}. Lista de palabras con + de 5 letras: {c[1]}")

tuplaPalabras(["jamon", "tijeras", "sol", "sal"])

