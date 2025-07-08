while True:
    print("\nMINI CALCULADORA")
    print("="*20)
    primer_numero = int(input("Ingrese el primer número: "))
    segundo_numero = int(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operacion (SUMA, RESTA, MULTIPLICACION, DIVISION): ")

    if operacion == "SUMA":
        resultado = primer_numero + segundo_numero
    elif operacion == "RESTA":
        resultado = primer_numero - segundo_numero
    elif operacion == "MULTIPLICACION":
        resultado = primer_numero * segundo_numero
    elif operacion == "DIVISION":
        resultado = primer_numero / segundo_numero
    else:
        print("Operación incorrecta")
        continue

    print(f"El resultado es: {resultado}")