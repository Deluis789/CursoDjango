# Profundizando tuplas

# Declaramos variables
a, b = 'Hola', 'Adios'
print(a, b)
# swap (intercambio)
a, b = b, a
print(a, b)

# Regresar múltiples valores en una funcion
def minmax(elementos):
    return min(elementos), max(elementos)

rmin, rmax = minmax([1,2,3,4,5])
print(f'Valor min: {rmin}, Valor max: {rmax}')

# Regresa la suma de una tupla
resultado = sum((1,2,3,4,5))
print(f'Resultado: {resultado}')

# Funcion suma
def suma(*args):
    return sum(args)

resultado = suma(1,2,3,4,5)
print(f'Resultado: {resultado}')