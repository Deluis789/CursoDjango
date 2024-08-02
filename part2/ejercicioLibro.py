"""EJERCICIO DE LIBROS"""
print('Proporciona los siguientes datos del libro:')
nombre = input('Proporciona el nombre del libro: ')
ide = int(input('Proporciona el ID: '))
precio = float(input('Proporciona el precio:'))
free = input('Indica si el envio es gratuito (True/False):')

if free == 'True':
    free = True
elif free == 'False':
    free = False
else:
    free = 'Valor incorrecto debe escribir True/Fase'

print(f'''
Nombre:{nombre}
Id:{ide}
Precio:{precio}
Envio Gratuito?:{free}  
''')

