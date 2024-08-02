# Definir una tupla
frutas = ('Naranja', 'Platano', 'Kiwi')
# Saber el largo de una tupla
print(len(frutas))
# Acceder a un elemento
print(frutas[0])
# Navegacion inversa
print(frutas[-1])
# Acceder a un rango sin incluir el ultimo indice
print(frutas[1:2])
# Recorrer elementos
for fruta in frutas:
    print(fruta, end=' ')
# Cambiar de valor tupla
frutasLista = list(frutas)
frutasLista[0] = 'Pomelo'
frutas = tuple(frutasLista)
print('\n', frutas)
# Eliminar Tupla
# del frutas
print(frutas)