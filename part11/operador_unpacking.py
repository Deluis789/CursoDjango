numeros = [1, 2, 3]
print(numeros)
print(*numeros)
print(*numeros, sep='-')

def suma(a, b, c):
    print(f'Resultado suma: {a + b + c}')

suma(*numeros)

# Listas
mi_lista = [2, 21, 5, 9, 54]
a, *b, c = mi_lista
print(a, b, c)

# Unir listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3}')
lista3 = [*lista1, *lista2]
print(f'Unir listas: {lista3}')

# Unir diccionarios
dic1 = {'A': 1, 'B': 2, 'C': 3}
dic2 = {'D': 4, 'E': 5}
dic3 = {**dic1, **dic2}
print(dic3)

# Construir una lista a partir de un str
lista = [*'holaMundo']
print(lista)
print(*lista, sep='')