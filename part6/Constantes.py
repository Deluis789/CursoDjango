MI_CONSTANTE = 'Valor de mi constante'


class Matematicas:
    PI = 3.1416


class Test:
    print(MI_CONSTANTE)
    # No  debemos cambiar el valor de una CONSTANTE
    MI_CONSTANTE = 'Nuevo valor'
    print(MI_CONSTANTE)
    print(Matematicas.PI)
