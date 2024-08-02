# Alcance de variables (scope)
var_global = 'Variable global'


def imprimir():
    print(f'Variabele global desde la funcion: {var_global}')
    # Definicion de variable local
    var_local = 'Variable local'
    print(f'Variable local de la funcion: {var_local}')

    def funcion_anidada():
        print(f'Variable local dentro de la funcion anidada: {var_local}')

    funcion_anidada()


# LLamamos a la funcion
imprimir()
print('PARTE 2 DE ALCANCE DE VARIABLES'.center(50, '-'))

def imprimir2():
    # Acceder a una variable global
    global var_global
    print(f'Variable global desde la funcion: {var_global}')
    # Cambiamos el valor de una variable global
    var_global = 'Nuevo valor'
    print(f'Nuevo valor de la variable global desde la funcion: {var_global}')


# LLamamos a la funcion
imprimir2()