'''
Crear una clase AgendaTelefonica que tenga los siguientes elementos:
Atributos: contactos (diccionario que contenga nombre -> número)
Métodos: añadir_contacto(contacto), modificar_contacto(contacto) y eliminar_contacto(contacto)
Consejo: el método update({clave: valor}) sirve para añadir o modificar un elemento, y el método pop(clave) elimina un elemento.
'''

class AgendaTelefonica:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"Contacto añadido! - {contacto}")
    
    def modificar_contacto(self, contacto):
        for c in self.contactos:
            if c["nombre"] == contacto["nombre"]:
                c["telefono"] = contacto["telefono"]
                print("¡Contacto modificado!")

    def eliminar_contacto(self, nombre):
        i = 0
        for c in self.contactos:
            if c["nombre"] == nombre:
                self.contactos.pop(i)
                print("¡Contacto eliminado!")
            i += 1

    def __str__(self):
        print(f"Lista de contactos: {self.contactos}")

ag = AgendaTelefonica()

ag.añadir_contacto({ "nombre": "Pepe", "telefono": 655464646})
ag.añadir_contacto({ "nombre": "Juan", "telefono": 666555666})

ag.__str__()


ag.modificar_contacto({ "nombre": "Juan", "telefono": 77755777})
ag.eliminar_contacto("Pepe")

ag.__str__()