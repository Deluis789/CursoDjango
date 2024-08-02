"""Definir una lista de tipo String"""
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# imprimir lista
print(nombres[-2])

# Imprimir un rango
print(nombres[0:2]) # Sin incluir el indice 2
# IR del inicio de la lista al indice sin incluiro
print(nombres[ :3]) # Esto va imprimir de indice 0 hasta el indice 3
print(nombres[0: ]) # Esto va imprimir del incice 0 hasta el ultimo elemento
# Cambio de valor al elemento
nombres[2] = 'Juana'
print(nombres)
# Para iterar el arreglo
for nombre in nombres:
    print(nombre)

else:
    print('Ya no hay mas elementos')
# Funcion len
print(len(nombres))
# Agregar elementos
nombres.append('Lorenzo')
print(nombres)
# Insertar un elemento en un indice especifico
nombres.insert(1,'Octavio')
print(nombres)
# Remover un elemento
nombres.remove('Juana')
print(nombres)
# Remover el ultimo elemento
nombres.pop()
print(nombres)
# Eliminar por indice
del nombres[0]
print(nombres)
# Eliminar toda la lista
nombres.clear()
print(nombres)
# Eliminar la lista de la memoria
# del nombres
print(nombres)