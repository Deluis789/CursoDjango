# Las funciones en python son ciudadanas de primer clase
# First class citizens

# Definimos la funcion
def sumar(a, b):
    return a + b

# 1. Asignar una funcion a una variable (no se usan parentesis)
mi_funcion = sumar

# verificar el tipo de variable
print(type(mi_funcion))

# LLamamos a la funcion atraves de la variable
resultado = mi_funcion(5, 6)
print('resultado:', resultado)

# 2. Funcion como argumento
def operacion(a, b, sumar_arg):
    print(f'Resutlado de suma: {sumar_arg(a, b)}')

operacion(4, 5, sumar)

# 3. Podemos retornar una funcion
def retornar_funcion():
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'Resultado funcion retornada: {mi_funcion_retornada(6, 3)}')