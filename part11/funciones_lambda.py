# Funciones Lambda
# Son funciones anonimas

# No es posible asignar una funcion a una variable
# mi_funcion = def suma(a, b):return a + b

# Con una funcion lambda(anonima, sin nombre y una sola linea de codigo)
# No se necesita ageggar parentesis para los parametros
# No se necesita usar la palabra return, pero si debe regresar una expresion

mi_funcion_lambda = lambda a, b: a + b

resultado = mi_funcion_lambda(5, 6)

print(f'Resultado de suma con función lambda: {resultado}')

# Funcion lambda que no recibe argumentos (debemos regresar una expresión valida)

mi_funcion_lambda = lambda: 'Funcion sin argumentos'

print(f'Llamar funcion lambda sin argumentos:{mi_funcion_lambda()}')

mi_funcion_lambda = lambda a = 2, b = 3: a + b

print(f'Resultado sin argumentos: {mi_funcion_lambda()}')
# Función lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)

print(f'Resultado argumentos variables: {mi_funcion_lambda(1, 2, 3, a=5, b=6)}')


