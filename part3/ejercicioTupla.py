"""CREAR UNA LISTA SOLO INCLUYA LOS NUMEROS MENORES A 5"""

tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

