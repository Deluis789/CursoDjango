# def descendente(numeros):
#     for numero in range(numeros, 0, -1):
#         print(numero)
#
#
# descendente(5)


# Otra forma de ser la funcion
def imprimit_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimit_numero_recursivo(numero - 1)
    elif numero == 0:
        return print('El valor es 0')
    elif numero < 0:
        print('Valor incorrecto')


imprimit_numero_recursivo(0)
