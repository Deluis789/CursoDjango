# help(str.capitalize)

mensaje = 'hola mundo'
mensaje2 = mensaje.capitalize()
print(mensaje, hex(id(mensaje)))
print(f'Mensaje 2: {mensaje2}, id:{hex(id(mensaje2))}')

# La misma variable pero direccion de memoria distinta esto quiero decir
# que son inmutables porque se crea siempre un objeto en un nuevo espacio en la memoria
mensaje += 'adios'
print(mensaje, hex(id(mensaje)))