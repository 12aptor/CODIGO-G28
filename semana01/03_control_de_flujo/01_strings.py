""" Strings en Python """
texto = "Python 🐍 es un lenguaje de programación muy potente"

""" Recorrer un string """
for caracter in texto:
    print(caracter)

""" Concatenar strings """
texto_concatenado = texto + " y fácil de aprender"
print(texto_concatenado)

""" Formatear strings """
nombre = "Pepito"
edad = 30
saludo = "Hola {}, tu edad es {} años".format(nombre, edad)
print(saludo)
segundo_saludo = f"Hola {nombre}, tu edad es {edad} años"
print(segundo_saludo)
tercer_saludo = "Hola %s, tu edad es %d años" % (nombre, edad)
print(tercer_saludo)

""" Métodos de strings """

""" .upper() """
print("upper()", texto.upper())

""" .lower() """
print("lower()", texto.lower())

""" .capitalize() """
print("capitalize()", texto.capitalize())

""" .count() """
print("count()", texto.count("Python"))

""" .replace() """
print("replace()", texto.replace("Python", "Rust"))

""" .split() """
print("split()", texto.split(" "))

""" .join() """
print("join()", texto.join(" "))

""" .strip() """
print("strip()", texto.strip())