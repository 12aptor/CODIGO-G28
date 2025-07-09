usuario = {
    "id": 1,
    "nombre": "Jhon Doe",
    "email": "jhon@gmail.com",
    "edad": 25,
    "estado": True,
}
print(usuario)

""" Constructor de diccionarios """
usuario_2 = dict(id=2, nombre="Anna Doe", email="anna@gmail.com", edad=30, estado=False)
print(usuario_2)

""" Acceder a los valores de un diccionario """
print(usuario["nombre"])
print(usuario.get("edad"))

""" Cambiar un valor de un diccionario """
usuario["nombre"] = "Jhon Doe Jr."
usuario["genero"] = "Masculino"
print(usuario)

""" Eliminar un valor de un diccionario """
del usuario["genero"]
usuario.pop("edad")
print(usuario)

""" Métodos de diccionarios """
print(usuario.keys()) # Devuelve una lista con las claves
print(usuario.values()) # Devuelve una lista con los valores
print(usuario.items()) # Devuelve una lista con pares clave-valor dentro de una tupla

""" Iterar sobre un diccionario """
for key, value in usuario.items():
    print(f"{key}: {value}")

for key in usuario:
    print(f"{key}: {usuario[key]}")