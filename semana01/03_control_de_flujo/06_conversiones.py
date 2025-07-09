# Programa tiene que convertir soles a dolares y viceversa

import os
import time

condicion = True
while condicion:
    print("""
    =================================
        CONVERSIONES DE UNIDADES
    =================================
        [1] Convertir soles a dolares
        [2] Convertir dolares a soles
        [3] Salir
    =================================
    """)
    opcion = int(input("Ingrese la opción deseada: "))
    
    if opcion == 1:
        cantidad = int(input("Ingrese la cantidad de soles: "))
        dolares = round(cantidad * 3.57, 2)
        print(f"El monto en dolares es: {dolares}")
    elif opcion == 2:
        cantidad = int(input("Ingrese la cantidad de dolares: "))
        soles = round(cantidad / 3.57, 2)
        print(f"El monto en soles es: {soles}")
    elif opcion == 3:
        print("Saliendo del programa...")
        condicion = False
    else:
        print("Opción incorrecta")

    time.sleep(2)
    os.system("cls")
    os.system("clear")