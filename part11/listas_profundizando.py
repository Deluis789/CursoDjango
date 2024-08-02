# profundizando en listas
# Listas son mutables
nombres1 = ['Juan', 'Karla', 'Pedro']
nombres2 = 'Laura Maria Gonzalo Ernesto'.split()
# Sumar listas
print(f'Sumar listas: {nombres1 + nombres2}')
# Extender una lista con otra lista
nombres1.extend(nombres2)
print(f'Extender lista 1: {nombres1}')

# Lista de números
numeros1 = [10, 40, 50, 4, 20, 90, 4]
# obtener el indice del primer elemento encontrado en una lista
# help(list.index)
print(f'Indice 4: {numeros1.index(4)}')
# Invertir el orden de los elementos de una lista
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

# Ordenar los elementos de una lista ascendente
numeros1.sort()
print('Lista ordenada ascendente:', numeros1)
# Ordenar los elementos de una lista descendente
numeros1.sort(reverse=True)
print('Lista ordenada descendente:', numeros1)

# Obtener el valor min y max de una lista
print(f'Valor minimo: {min(numeros1)}')
print(f'Valor minimo: {max(numeros1)}')

# Copiar los elementos de una lista
numeros2 = numeros1.copy()
# help(list.copy)
print(numeros1)
print(numeros2)
print(f'Misma referencia: {numeros1 is numeros2}')
print(f'Tiene el mismo contenido: {numeros1 == numeros2}')

# Podemos usar el constructor de la lista
numeros2 = list(numeros1)
print(f'Misma referencia: {numeros1 is numeros2}')
print(f'Tiene el mismo contenido: {numeros1 == numeros2}')

# Otra forma de copiar una lsita
# slicing
numeros2 = numeros1[:]
print(numeros2)

