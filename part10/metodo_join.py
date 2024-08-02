# help(str.join)
""" ESTO ES UNA ITERABLE PUEDEN SER:
TUPLAS, DICCIONARIOS, LISTAS"""

tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
mensaje = '* '.join(tupla_str)

print(f'Mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)

print(f'Mensaje 2: {mensaje}')

cadena = 'HolaMundo'
mensaje = '- '.join(cadena)
print(mensaje)
""" NO  SE PUEDEN TENER VALORES INT"""
diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': '18'}
llaves = ', '.join(diccionario.keys())
values = '* '.join(diccionario.values())

print(f'llaves: {llaves} tipo: {type(llaves)}')
print(f'valores: {values} tipo: {type(values)}')
