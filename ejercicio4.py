'''
Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro, e imprima cada multiplicación con el formato “<A> x <B> = <C>”.
Hacer una primera versión con un bucle.
Hacer otra versión con comprensión de listas.
'''

# Version bucle
def imprimirTabla(num):
    print("Esta es la tabla del número", num)
    for i in range(11):
        print(f"{num} x {i} = {num*i}")

imprimirTabla(5)

# Version compresion lista

def imprimirTablaLista(num):
    print("Esta es la tabla del número", num)
    lista = [num*i for i in range(11)]
    print(lista)

imprimirTablaLista(5)