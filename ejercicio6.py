'''
Crear una función que calcule el factorial de un número, e imprima por consola “El factorial de <X> es <Y>”.
'''

def factorial(num):
    factorial = 1
    for i in range(2, num+1):
        factorial = factorial * i

    print(f"El factorial de {num} es {factorial}")

factorial(5)