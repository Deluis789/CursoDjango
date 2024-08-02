# Funciones anidadas

def calculadora(a, b, operacion='sumar'):
    # 1. Definir Funciones anidadas
    def sumar(c, d):
        return c + d

    def restar(c, d):
        return c - d

    # 2. Llamammos a la funciones anidadas
    if operacion == 'sumar':
        print(f'Resultado de la suma es: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'La resta es: {restar(a, b)}')


# La suma esta en la funcion por default
calculadora(5, 5)
calculadora(5, 6, operacion='restar')
