""" EJERCICIO  UNO INSERTAR EN UNA FUNCION """


def uno(lst):
    print('listas=', lst)
    print('Insertar al final de la lista')
    lst.append(10)
    print(lst)
    print('Concatenacion:')
    lst.extend([10, 20, 30])
    print(lst)


uno([6, 9, 7, 8, 4])

""" EJERCICIO 2 """

lista = []
lista.insert(0,5)
lista.insert(1,'hola')
print(lista)
print(lista.index(5))
print(lista.count(0))
print(lista.pop(0))