# Multiplicacion de listas
lista_multiplicacion = 5*[[2, 5]]
print(lista_multiplicacion)
print(f'Tienen la misma referencia: {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Son el mismo contenido:{lista_multiplicacion[0] == lista_multiplicacion[1]}')
# Aqui se agrega un elemnto a la lista y como tienen la misma direccion de memoria afecta a todos los elemntos
lista_multiplicacion[2].append(12)
print(lista_multiplicacion)
#####
# Matrices en python
matriz = [[10, 25], [25, 50, 65], [45, 89, 12, 23]]
print(f'Matriz original: {matriz}')
print(f'Renglon 0, Columna 0: {matriz[0][0]}')
# Cambiar el valor a un elemento de una matriz
matriz[2][0] = 25
print(f'Matriz modificada: {matriz}')

# Ordenear listas segun el largo de listas
lista_listas = [[10, 14, 87, 90, 71], [5, 6, 3, 4], [3, 5, 23, 123, 55, 63, 87]]
lista_listas.sort(key=len)
print(f'Ordenas listas segun el largo: {lista_listas}')

# sorted built-in
# help (sorted)
# Ordenar de manera ascendente segun el abecedario
nombres1 = ['Juan', ' Carlos', 'Neysarmiento', 'Nicolas']
nombres1 = sorted(nombres1)
print(f'Listar de forma ascendente:{nombres1}')
# Ordenar de manera ascendente segun el descendente
nombres1 = sorted(nombres1, reverse=True)
print(f'Listar de forma descendente:{nombres1}')
# Ordenar por la cantidad de caracteres
nombres1 = sorted(nombres1,key=len)
print(nombres1)
# build-in reversed tuplas y listas
nombres1 = reversed(nombres1)
print(list(nombres1))