'''
Crear una función que reciba una temperatura en Celsius como parámetro, e imprima por consola las equivalencias en Fahrenheit y Kelvin
'''

def conversorCelsius(temp):
    fahrenheit = (temp * 9 / 5) + 32
    kelvin = temp + 273.15

    print(f"{temp} ºC equivalen a {fahrenheit}º F y {kelvin}º K") 

conversorCelsius(32)