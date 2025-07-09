""" Crear un generador de contraseñas seguras. El
programa debe pedir la longitud de la contraseña"""


import string
import random

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)
    return contrasena
    

def main():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    contrasena = generar_contrasena(longitud)
    print(f"Tu contraseña segura es: {contrasena}")

if __name__ == "__main__":
    main()