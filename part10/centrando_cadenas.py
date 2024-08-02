# center - Centrar un str

titulo = 'Sitio web Diaz'
# print(len(titulo))
print(titulo.center(50,'*'))
print(len(titulo.center(50,'*')))
# Alineando a la izquierda y a la derecha
print(titulo.ljust(50,'-'))
print(titulo.rjust(50,'-'))

# Método Replace
mensaje = 'hola que tal ¿como estas?'
print(mensaje.replace(' ', '*'))

# Método Strip
mensaje = '***hola que tal ¿como estas?***'
print(mensaje.strip())
print(mensaje.lstrip('*'))
print(mensaje.rstrip('*'))
