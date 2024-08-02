# print(dir(__builtins__)) ///PARA VER TODOS LOS METODOS DENTRO DE PYTHON
# help(zip)

numeros = [1, 2, 3]
letras = ['A', 'B', 'C']
mezcla = zip(numeros, letras)
print(mezcla)
print(list(mezcla))
print(tuple(zip(letras, numeros)))
print('Mas Detalles'.center(50, '*'))
numeros = (1, 2, 3)
letras = ['A', 'B', 'C', 'D']
indentificadores = 125, 562, 232, 333
conjunto = {3,4,12,44,43,21,2,6}
mezcla = zip(numeros, letras, indentificadores, conjunto)
print(list(mezcla))

# Iterar en paralelo
nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros, letras, indentificadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)

# Unzip
mezcla = [(1,'a'),(2,'b'),(3,'c')]
numeros, letras = zip(*mezcla)
print(f'Numeros: {numeros}, Letras: {letras}')

# Ordenamiento usando zip
letras = ['c','d','a','e','b']
numeros = [3,2,4,1,0]
mezcla = zip(letras, numeros)
# Sin orden
print(tuple(mezcla))
# Ordenar por letra (primer iterable)
print(sorted(zip(letras, numeros)))

# Crear un diccionario con zip y dos iterables
llaves = ['nombres','apellido','edad']
valores = ['Juan','Aliaga',42]
diccionario = dict(zip(llaves,valores))
print(diccionario)

# Actualizar un elemento de un diccionario
llave = ['nombres']
nuevo_nombre = ['Roberto']
diccionario.update(zip(llave, nuevo_nombre))
print(diccionario)
