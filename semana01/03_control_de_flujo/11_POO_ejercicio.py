""" Crear un programa que simule el funcionamiento de un cajero automático.
Deberá tener un menú con las siguientes opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar saldo disponible
Iniciar con un saldo de $1000.00 """

class Cajero:
    def __init__(self, saldo):
        self.saldo = saldo

    def ingresar_saldo(self, monto):
        if monto <= 0:
            print("Monto incorrecto")
            return
        self.saldo += monto
        print("Deposito exitoso")
        self.mostrar_saldo()

    def retirar_saldo(self, monto):
        if monto <= 0:
            print("Monto incorrecto")
            return
        
        if monto > self.saldo:
            print("Saldo insuficiente")
            return
        self.saldo -= monto
        print("Retiro exitoso")
        self.mostrar_saldo()

    def mostrar_saldo(self):
        print(f"\nSaldo disponible: {self.saldo}")

def main():
    cajero_bcp = Cajero(saldo=1000)

    while True:
        print("\n\n1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo disponible\n")

        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            monto = float(input("Ingrese el monto a depositar: "))
            cajero_bcp.ingresar_saldo(monto)

        elif opcion == 2:
            monto = float(input("Ingrese el monto a retirar: "))
            cajero_bcp.retirar_saldo(monto)
        elif opcion == 3:
            cajero_bcp.mostrar_saldo()
        elif opcion == 4:
            print("Gracias por visitarnos")
            break
        else:
            print("Opción incorrecta")

if __name__ == "__main__":
    main()