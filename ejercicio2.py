'''
Crear una clase Mascota que tenga los siguientes elementos:
Atributos: nombre, año de nacimiento y dueño (None por defecto)
Métodos: calcular_edad() y adoptar(nombre_dueño)
'''

class Mascota:
    def __init__(self, name, birth_year, owner=None):
        self.name = name
        self.birth_year = birth_year
        self.owner = owner

    def calcular_edad(self):
        print(f"{2025 - self.birth_year}")

    def adoptar(self, owner_name):
        self.owner = owner_name

m = Mascota("Pepita", 2015)

m.calcular_edad()

m.adoptar("Pepe")

print(m.owner)
