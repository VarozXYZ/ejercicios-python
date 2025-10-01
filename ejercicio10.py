'''
Crear una función que reciba dos sets como parámetros, e imprima:
Los elementos que están en ambos sets (intersección)
Los elementos que están solo en el primer set (diferencia)
Los elementos que están solo en el segundo set (diferencia)
Consejo: el operador intersección es &, y el operador diferencia es -.
'''

def setFilter(s1, s2):
    same = s1 & s2
    only_one = s1 - s2
    only_two = s2 - s1

    print(f"Los elementos en conjunto de ambos sets son: {same}")
    print(f"Los elementos que solo aparecen en el set 1 son: {only_one}")
    print(f"Los elementos que solo aparecen en el set 2 son: {only_two}")

set_one = { 5, 15, 20, "a", "b", "z" }

set_two = { 1, 10, 15, "x", "y", "z" }

setFilter(set_one, set_two)