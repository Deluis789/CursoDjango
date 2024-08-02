# bool contiene los valores de True y False
# Tipos numericos, False para 0, True demas valores
valor = 0
resultado = bool(valor)
print(f'Valor {valor}, {resultado}')
valor = 14
resultado = bool(valor)
print(f'Valor {valor}, {resultado}')

# Tipo str, False para '', True demás valores
valor = ''
resultado = bool(valor)
print(f'Valor {valor}, Resultado: {resultado}')
valor = 'hola'
resultado = bool(valor)
print(f'Valor {valor}, Resultado: {resultado}')

# Tipo colecciones, False para colecciones vacias, True para todas las demas colecciones
# Lista
valor = []
resultado = bool(valor)
print(f'Valor {valor}, Resultado: {resultado}')
valor = ['hola', 2, 3]
resultado = bool(valor)
print(f'Valor {valor}, Resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
print(f'Valor {valor}, Resultado: {resultado}')
valor = (5, 2, 6)
resultado = bool(valor)
print(f'Valor {valor}, Resultado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
print(f'Valor {valor}, Resultado: {resultado}')
valor = {'Nombre': 'Juan', 'Apellido': 'Perez'}
resultado = bool(valor)
print(f'Valor {valor}, Resultado: {resultado}')

# Condicioes
if '':
    print('Regresa verdadero')
else:
    print('Regresa Falso')

if bool(5):
    print('Regresa verdadero')
else:
    print('Regresa Falso')

# Ciclo While
variable = []
while variable:
    print('Inicia el ciclo while.')
    break
else:
    print('Fin ciclo while')

