'''
Crear una clase CuentaBancaria que tenga los siguientes elementos:
Atributos: titular, nombre_banco y saldo
Métodos: ingresar(cantidad) y retirar(cantidad)
'''

class CuentaBancaria: 
    def __init__(self, titular, nombre_banco, saldo):
        self.titular = titular
        self.nombre_banco = nombre_banco
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print(f"Ingresados {cantidad}€")

    def retirar(self, cantidad):
        if (cantidad <= self.saldo):
            self.saldo = self.saldo - cantidad
            print(f"Retirados {cantidad}€")
        else:
            print(f"No se puede retirar {cantidad}€ porque tu saldo es inferior a dicha cantidad ({self.saldo}€)")
    
    def __str__(self):
        print(f"Titular de la cuenta: {self.titular}\nBanco: {self.nombre_banco}\nSaldo: {self.saldo}€")

cuenta = CuentaBancaria("Alvaro Rodriguez", "BBVA", 5000)
cuenta.__str__()

cuenta.ingresar(2000)

cuenta.retirar(10000)

cuenta.retirar(5000)