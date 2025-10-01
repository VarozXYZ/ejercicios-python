'''
Crear una clase AgendaTelefonica que tenga los siguientes elementos:
Atributos: contactos (diccionario que contenga nombre -> número)
Métodos: añadir_contacto(contacto), modificar_contacto(contacto) y eliminar_contacto(contacto)
Consejo: el método update({clave: valor}) sirve para añadir o modificar un elemento, y el método pop(clave) elimina un elemento.
'''

class AgendaTelefonica:
    def __init__(self, contactos={}):
        self.contactos = contactos

    def añadir_contacto(self, nombre, telefono):
        self.contactos.update({ nombre: telefono})
        print(f"¡Contacto añadido! - {nombre}: {telefono}")
    
    def modificar_contacto(self, nombre, telefono):
        self.contactos.update({ nombre: telefono})
        print(f"¡Contacto modificado! - {nombre}: {telefono}")

    def eliminar_contacto(self, nombre):
        self.contactos.pop(nombre)
        print(f"¡Contacto borrado!")

    def __str__(self):
        print(f"Lista de contactos: {self.contactos}")

ag = AgendaTelefonica()

ag.añadir_contacto("Pepe", 655464646)
ag.añadir_contacto("Juan", 666777666)

ag.__str__()


ag.modificar_contacto("Pepe", 788555788)
ag.__str__()
ag.eliminar_contacto("Pepe")

ag.__str__()