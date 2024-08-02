def suma(a, b):
    return a + b


resultado = suma(5, 6.6)
print('La suma es:', resultado)


# Funciones con valor por default
def sumas(a=2, b=3):
    return a + b


print(f'La suma por default es:{sumas()}')
print(f'La suma sobreescrita es:{sumas(6, 6)}')
