""" Listas en Python """
lista = ["Python", "Rust", "Go", "Typescript", "JavaScript", "C++"]

""" Acceder a elementos """
print(lista[0])

""" Rango de elementos """
print(lista[0:3])
# 0 (inicio): primer índice incluido (0)
# 3 (fin): primer índice excluido (3)

""" Acceso a rango de elementos con salto """
print(lista[0:4:2])
# 0 (inicio): primer índice incluido (0)
# 4 (fin): primer índice excluido (4)
# 2 (paso): toma cada 2 elementos

""" Acceso negativo """
print(lista[-1])

""" Acceso a rango desde inicio  """
print(lista[-3:])

""" Agregar elementos """
lista.append("C#")

""" Eliminar elementos por índice """
lista.pop(0)

""" Eliiminar elementos por valor """
lista.remove("Rust")

""" Eliminar todos los elementos """
lista.clear()

""" Invertir la lista """
lista.reverse()

""" Ordenar la lista """
lista.sort()