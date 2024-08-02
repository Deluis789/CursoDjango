# Profundizando en el tipo str

# caracteres de escape
resultado = 'Hola\'Mundo'
print(f'Resultado: {resultado}')

# Backspace
resultado = 'Se borrara el ultimo elemento.\b\b'
print(f'Resultado: {resultado}')

# Caracter \
resultado = 'c:\\nuevo\\juan'
print(f'Resultado: {resultado}')
resultado = 'c:\nuevo\\juan'
print(f'Resultado: {resultado}')

# Row
resultado = r'Caracter de salto \n de linea'
print(f'Resultado: {resultado}')